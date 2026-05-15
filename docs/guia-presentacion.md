# Guia de Presentacion - Mini Proyecto de Analisis de Datos con Python

## 1. Pitch breve

Este proyecto complementa un dashboard de Business Intelligence desarrollado en Power BI. Use el mismo dataset de una ferreteria, pero en este caso trabaje el analisis tecnico con Python: limpieza, validacion, transformacion, analisis descriptivo, visualizaciones e insights.

El objetivo fue demostrar que puedo trabajar no solo la visualizacion final, sino tambien la preparacion y explicacion tecnica de los datos.

## 2. Problema que resuelve

El dashboard de BI permite monitorear indicadores comerciales, pero era necesario contar con un analisis reproducible que explique:

- como fueron limpiados los datos,
- si los datos eran consistentes,
- que productos y categorias explicaban las ventas,
- como evolucionaban las ventas en el tiempo,
- y que relacion existia entre precio y unidades vendidas.

## 3. Dataset utilizado

Use el mismo dataset del Proyecto 1:

- `productos.csv`
- `ventas.csv`

El dataset contiene informacion de productos, categorias, costos, stock, fechas, cantidades, precios unitarios y ventas totales.

## 4. Proceso realizado

### 1. Exploracion inicial

Revise dimensiones, columnas, tipos de datos, valores nulos y duplicados.

### 2. Limpieza y transformacion

Normalice nombres de columnas, converti fechas y campos numericos, limpie textos y valide el calculo del total de venta.

### 3. Integracion de datos

Uni ventas con el catalogo de productos para agregar ID de producto, costo y stock.

### 4. Variables derivadas

Cree nuevas variables como:

- periodo,
- trimestre,
- margen unitario,
- margen estimado,
- margen porcentual.

### 5. Analisis descriptivo

Calcule KPIs generales, rankings de productos, resumen por categoria, resumen mensual y ranking por margen.

### 6. Visualizaciones

Genere graficos de tendencia mensual, top productos, ventas por categoria y relacion precio vs unidades vendidas. Tambien deje un pipeline reproducible en `src/pipeline_analisis.py` para reconstruir los datasets procesados, reportes y figuras desde los CSV originales.

## 5. Resultados clave

| Indicador | Resultado |
|---|---:|
| Ventas totales | S/ 128,182.96 |
| Unidades vendidas | 8,056 |
| Transacciones | 1,800 |
| Margen estimado | S/ 35,775.12 |
| Margen estimado % | 27.91% |

## 6. Insights principales

- Materiales de construccion concentra la mayor parte de las ventas.
- Cemento bolsa 42.5 kg es el producto lider.
- Herramientas electricas genera ingresos importantes con pocas unidades por su mayor precio promedio.
- Productos como arena fina y ladrillo pandereta tienen alta rotacion.
- La correlacion entre precio promedio y unidades vendidas es negativa: aproximadamente -0.3247.

## 7. Diferencia entre Power BI y Python

Power BI me permite comunicar los indicadores de forma visual e interactiva.

Python me permite demostrar el proceso tecnico: cargar, limpiar, validar, transformar, analizar y explicar los datos de forma reproducible.

Una forma simple de decirlo en entrevista:

> Power BI muestra que esta pasando; Python demuestra como prepare y valide los datos para llegar a esos resultados.

## 8. Que podria mejorar en una siguiente version

- Agregar analisis de baja rotacion e inventario.
- Crear segmentacion de productos por ventas, margen y stock.
- Analizar estacionalidad por mes o trimestre.
- Agregar pruebas automatizadas para validar datos.
- Convertir el pipeline en paquete instalable o tarea automatizada.

## 9. Como defender el proyecto en entrevista

Primero explicaria el contexto del Proyecto 1 en Power BI. Luego diria que este Proyecto 2 busca complementar ese dashboard desde el lado tecnico.

Despues mostraria el notebook en este orden:

1. Exploracion inicial.
2. Limpieza y validacion.
3. Dataset limpio.
4. KPIs y rankings.
5. Visualizaciones.
6. Insights.
7. Diferencia entre BI y Python.

Cerraria diciendo que el proyecto demuestra un flujo completo: desde datos crudos hasta analisis explicable y publicable en GitHub.
