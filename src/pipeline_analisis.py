from __future__ import annotations

import json
import unicodedata
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
REPORTS = PROJECT_ROOT / "reports"
FIGURES = REPORTS / "figures"


def normalizar_columna(nombre_columna: str) -> str:
    """Convierte nombres de columnas a snake_case ASCII."""
    texto = unicodedata.normalize("NFKD", str(nombre_columna))
    texto = "".join(caracter for caracter in texto if not unicodedata.combining(caracter))
    return texto.strip().lower().replace(" ", "_")


def limpiar_textos(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for columna in df.select_dtypes(include=["object", "string"]).columns:
        df[columna] = df[columna].astype(str).str.strip()
    return df


def cargar_datos() -> tuple[pd.DataFrame, pd.DataFrame]:
    productos = pd.read_csv(DATA_RAW / "productos.csv")
    ventas = pd.read_csv(DATA_RAW / "ventas.csv")
    productos.columns = [normalizar_columna(col) for col in productos.columns]
    ventas.columns = [normalizar_columna(col) for col in ventas.columns]
    return productos, ventas


def limpiar_y_transformar(productos: pd.DataFrame, ventas: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    productos_limpio = limpiar_textos(productos).rename(columns={"nombre": "producto"})
    ventas_limpio = limpiar_textos(ventas)

    productos_limpio["costo"] = pd.to_numeric(productos_limpio["costo"], errors="coerce")
    productos_limpio["stock"] = pd.to_numeric(productos_limpio["stock"], errors="coerce").astype("Int64")

    ventas_limpio["fecha"] = pd.to_datetime(ventas_limpio["fecha"], errors="coerce")
    ventas_limpio["cantidad"] = pd.to_numeric(ventas_limpio["cantidad"], errors="coerce").astype("Int64")
    ventas_limpio["precio_unitario"] = pd.to_numeric(ventas_limpio["precio_unitario"], errors="coerce")
    ventas_limpio["total"] = pd.to_numeric(ventas_limpio["total"], errors="coerce")

    ventas_limpio["total_calculado"] = (
        ventas_limpio["cantidad"].astype(float) * ventas_limpio["precio_unitario"]
    ).round(2)
    ventas_limpio["diferencia_total"] = (
        ventas_limpio["total"] - ventas_limpio["total_calculado"]
    ).round(2)

    ventas_enriquecidas = ventas_limpio.merge(
        productos_limpio[["id_producto", "producto", "categoria", "costo", "stock"]],
        on="producto",
        how="left",
        suffixes=("_venta", "_catalogo"),
    )

    ventas_enriquecidas["categoria"] = ventas_enriquecidas["categoria_catalogo"].fillna(
        ventas_enriquecidas["categoria_venta"]
    )
    ventas_enriquecidas["margen_unitario"] = (
        ventas_enriquecidas["precio_unitario"] - ventas_enriquecidas["costo"]
    ).round(2)
    ventas_enriquecidas["margen_estimado"] = (
        ventas_enriquecidas["margen_unitario"] * ventas_enriquecidas["cantidad"].astype(float)
    ).round(2)
    ventas_enriquecidas["margen_pct"] = (
        ventas_enriquecidas["margen_estimado"] / ventas_enriquecidas["total"]
    ).round(4)
    ventas_enriquecidas["anio"] = ventas_enriquecidas["fecha"].dt.year
    ventas_enriquecidas["mes"] = ventas_enriquecidas["fecha"].dt.month
    ventas_enriquecidas["periodo"] = ventas_enriquecidas["fecha"].dt.to_period("M").astype(str)
    ventas_enriquecidas["trimestre"] = ventas_enriquecidas["fecha"].dt.to_period("Q").astype(str)

    ventas_limpias = ventas_enriquecidas[
        [
            "fecha",
            "periodo",
            "anio",
            "mes",
            "trimestre",
            "id_producto",
            "producto",
            "categoria",
            "cantidad",
            "precio_unitario",
            "total",
            "total_calculado",
            "diferencia_total",
            "costo",
            "margen_unitario",
            "margen_estimado",
            "margen_pct",
            "stock",
        ]
    ].sort_values(["fecha", "producto"]).reset_index(drop=True)

    productos_limpios = productos_limpio.copy()
    productos_limpios["valor_inventario"] = (
        productos_limpios["costo"] * productos_limpios["stock"]
    ).round(2)

    return productos_limpios, ventas_limpias


def crear_tablas_analiticas(ventas_limpias: pd.DataFrame) -> dict[str, pd.DataFrame]:
    ranking_productos = (
        ventas_limpias.groupby(["id_producto", "producto", "categoria"], as_index=False)
        .agg(
            ventas_totales=("total", "sum"),
            unidades_vendidas=("cantidad", "sum"),
            transacciones=("producto", "count"),
            margen_estimado=("margen_estimado", "sum"),
            precio_promedio=("precio_unitario", "mean"),
        )
        .sort_values("ventas_totales", ascending=False)
    )
    ranking_productos["margen_pct"] = (
        ranking_productos["margen_estimado"] / ranking_productos["ventas_totales"]
    ).round(4)

    resumen_categorias = (
        ventas_limpias.groupby("categoria", as_index=False)
        .agg(
            ventas_totales=("total", "sum"),
            unidades_vendidas=("cantidad", "sum"),
            transacciones=("producto", "count"),
            margen_estimado=("margen_estimado", "sum"),
            precio_promedio=("precio_unitario", "mean"),
        )
        .sort_values("ventas_totales", ascending=False)
    )
    resumen_categorias["participacion_ventas_pct"] = (
        resumen_categorias["ventas_totales"] / resumen_categorias["ventas_totales"].sum()
    ).round(4)
    resumen_categorias["margen_pct"] = (
        resumen_categorias["margen_estimado"] / resumen_categorias["ventas_totales"]
    ).round(4)

    resumen_mensual = (
        ventas_limpias.groupby("periodo", as_index=False)
        .agg(
            ventas_totales=("total", "sum"),
            unidades_vendidas=("cantidad", "sum"),
            transacciones=("producto", "count"),
            margen_estimado=("margen_estimado", "sum"),
            ticket_promedio=("total", "mean"),
        )
        .sort_values("periodo")
    )
    resumen_mensual["variacion_ventas_pct"] = resumen_mensual["ventas_totales"].pct_change().round(4)
    resumen_mensual["media_movil_3m"] = (
        resumen_mensual["ventas_totales"].rolling(window=3, min_periods=1).mean()
    ).round(2)

    ranking_margen = ranking_productos.sort_values("margen_estimado", ascending=False)

    return {
        "ranking_productos": ranking_productos,
        "resumen_categorias": resumen_categorias,
        "resumen_mensual": resumen_mensual,
        "ranking_margen_productos": ranking_margen,
    }


def crear_reporte_calidad(productos_limpios: pd.DataFrame, ventas_limpias: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "validacion": "productos_total",
                "valor": len(productos_limpios),
                "estado": "OK",
                "detalle": "Cantidad de productos en catalogo limpio",
            },
            {
                "validacion": "ventas_total",
                "valor": len(ventas_limpias),
                "estado": "OK",
                "detalle": "Cantidad de registros en ventas limpias",
            },
            {
                "validacion": "nulos_ventas_limpias",
                "valor": int(ventas_limpias.isna().sum().sum()),
                "estado": "OK" if int(ventas_limpias.isna().sum().sum()) == 0 else "Revisar",
                "detalle": "Valores nulos en dataset limpio de ventas",
            },
            {
                "validacion": "nulos_productos_limpios",
                "valor": int(productos_limpios.isna().sum().sum()),
                "estado": "OK" if int(productos_limpios.isna().sum().sum()) == 0 else "Revisar",
                "detalle": "Valores nulos en dataset limpio de productos",
            },
            {
                "validacion": "ventas_sin_producto",
                "valor": int(ventas_limpias["id_producto"].isna().sum()),
                "estado": "OK" if int(ventas_limpias["id_producto"].isna().sum()) == 0 else "Revisar",
                "detalle": "Ventas sin producto asociado",
            },
            {
                "validacion": "totales_mal_calculados",
                "valor": int((ventas_limpias["diferencia_total"].abs() > 0.01).sum()),
                "estado": "OK"
                if int((ventas_limpias["diferencia_total"].abs() > 0.01).sum()) == 0
                else "Revisar",
                "detalle": "Diferencia entre total original y total recalculado",
            },
        ]
    )


def exportar_datos(
    productos_limpios: pd.DataFrame,
    ventas_limpias: pd.DataFrame,
    tablas: dict[str, pd.DataFrame],
    reporte_calidad: pd.DataFrame,
) -> None:
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)

    productos_limpios.to_csv(DATA_PROCESSED / "productos_limpios.csv", index=False, encoding="utf-8-sig")
    ventas_limpias.to_csv(DATA_PROCESSED / "ventas_limpias.csv", index=False, encoding="utf-8-sig")

    for nombre, tabla in tablas.items():
        tabla.to_csv(DATA_PROCESSED / f"{nombre}.csv", index=False, encoding="utf-8-sig")

    reporte_calidad.to_csv(REPORTS / "quality_report.csv", index=False, encoding="utf-8-sig")


def exportar_figuras(tablas: dict[str, pd.DataFrame]) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")

    resumen_mensual = tablas["resumen_mensual"]
    ranking_productos = tablas["ranking_productos"]
    resumen_categorias = tablas["resumen_categorias"]

    plt.figure(figsize=(12, 5))
    sns.lineplot(data=resumen_mensual, x="periodo", y="ventas_totales", marker="o", label="Ventas mensuales")
    sns.lineplot(data=resumen_mensual, x="periodo", y="media_movil_3m", marker="o", label="Media movil 3M")
    plt.title("Tendencia mensual de ventas", fontsize=14, fontweight="bold")
    plt.xlabel("Periodo")
    plt.ylabel("Ventas totales (S/)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIGURES / "01_tendencia_mensual_ventas.png", dpi=150, bbox_inches="tight")
    plt.close()

    top_productos = ranking_productos.head(10).sort_values("ventas_totales", ascending=True)
    plt.figure(figsize=(11, 6))
    sns.barplot(data=top_productos, x="ventas_totales", y="producto", hue="producto", palette="Blues_r", legend=False)
    plt.title("Top 10 productos por ventas", fontsize=14, fontweight="bold")
    plt.xlabel("Ventas totales (S/)")
    plt.ylabel("Producto")
    plt.tight_layout()
    plt.savefig(FIGURES / "02_top_productos_ventas.png", dpi=150, bbox_inches="tight")
    plt.close()

    categorias = resumen_categorias.sort_values("ventas_totales", ascending=True)
    plt.figure(figsize=(11, 6))
    sns.barplot(data=categorias, x="ventas_totales", y="categoria", hue="categoria", palette="viridis", legend=False)
    plt.title("Ventas por categoria", fontsize=14, fontweight="bold")
    plt.xlabel("Ventas totales (S/)")
    plt.ylabel("Categoria")
    plt.tight_layout()
    plt.savefig(FIGURES / "03_ventas_por_categoria.png", dpi=150, bbox_inches="tight")
    plt.close()

    productos_precio_unidades = ranking_productos[ranking_productos["unidades_vendidas"] > 0].copy()
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=productos_precio_unidades,
        x="precio_promedio",
        y="unidades_vendidas",
        size="ventas_totales",
        hue="categoria",
        sizes=(40, 500),
        alpha=0.75,
    )
    plt.title("Relacion precio promedio vs unidades vendidas", fontsize=14, fontweight="bold")
    plt.xlabel("Precio promedio unitario (S/)")
    plt.ylabel("Unidades vendidas")
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig(FIGURES / "04_precio_vs_unidades.png", dpi=150, bbox_inches="tight")
    plt.close()


def crear_resumen_ejecutivo(tablas: dict[str, pd.DataFrame], ventas_limpias: pd.DataFrame) -> dict[str, object]:
    ranking_productos = tablas["ranking_productos"]
    resumen_categorias = tablas["resumen_categorias"]
    resumen_mensual = tablas["resumen_mensual"]
    productos_precio_unidades = ranking_productos[ranking_productos["unidades_vendidas"] > 0].copy()

    return {
        "ventas_totales": round(float(ventas_limpias["total"].sum()), 2),
        "unidades_vendidas": int(ventas_limpias["cantidad"].sum()),
        "transacciones": int(len(ventas_limpias)),
        "margen_estimado": round(float(ventas_limpias["margen_estimado"].sum()), 2),
        "margen_estimado_pct": round(float(ventas_limpias["margen_estimado"].sum() / ventas_limpias["total"].sum()), 4),
        "top_producto": str(ranking_productos.iloc[0]["producto"]),
        "top_categoria": str(resumen_categorias.iloc[0]["categoria"]),
        "mejor_mes": str(resumen_mensual.loc[resumen_mensual["ventas_totales"].idxmax(), "periodo"]),
        "correlacion_precio_unidades": round(
            float(productos_precio_unidades[["precio_promedio", "unidades_vendidas"]].corr().iloc[0, 1]),
            4,
        ),
    }


def main() -> None:
    productos, ventas = cargar_datos()
    productos_limpios, ventas_limpias = limpiar_y_transformar(productos, ventas)
    tablas = crear_tablas_analiticas(ventas_limpias)
    reporte_calidad = crear_reporte_calidad(productos_limpios, ventas_limpias)

    exportar_datos(productos_limpios, ventas_limpias, tablas, reporte_calidad)
    exportar_figuras(tablas)

    resumen = crear_resumen_ejecutivo(tablas, ventas_limpias)
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "resumen_ejecutivo.json").write_text(
        json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(json.dumps(resumen, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
