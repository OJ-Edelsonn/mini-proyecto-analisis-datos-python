# Documento Maestro - Mini Proyecto: Analisis de Datos con Python

## 1. Resumen del Proyecto

Este proyecto consiste en desarrollar un analisis tecnico con Python usando el mismo dataset del Proyecto 1: **Sistema de Business Intelligence - Ferreteria**.

El objetivo es complementar el dashboard de Power BI con un flujo reproducible de limpieza, transformacion, analisis descriptivo, visualizacion y generacion de insights usando Python, Pandas y Jupyter Notebook.

## 2. Objetivo General

Demostrar capacidad de analisis de datos con Python mediante un proyecto completo, ordenado y explicable en una entrevista de trabajo.

## 3. Objetivos Especificos

- Usar el dataset original del Proyecto 1.
- Limpiar y transformar los datos con Pandas.
- Crear datasets limpios listos para analisis.
- Calcular metricas principales de ventas, productos, categorias y tiempo.
- Identificar productos mas vendidos y patrones relevantes.
- Analizar tendencias simples por periodo.
- Explorar la relacion entre precio y ventas.
- Documentar el proceso tecnico de forma clara.
- Preparar y publicar el proyecto en GitHub.

## 4. Alcance

### Incluye

- Notebook Jupyter con analisis paso a paso.
- Dataset limpio en formato CSV.
- Analisis descriptivo de ventas.
- Ranking de productos.
- Tendencias mensuales.
- Analisis basico de relacion precio vs ventas.
- Visualizaciones con Matplotlib y Seaborn.
- README del proyecto.
- Documento maestro.
- Guia de presentacion.
- Pipeline reproducible en `src/pipeline_analisis.py`.
- Publicacion en GitHub.

### No incluye

- Modelo predictivo avanzado.
- Machine Learning.
- Dashboard interactivo nuevo.
- Automatizacion productiva.
- Conexion a base de datos externa.

## 5. Dataset

Fuente: dataset del Proyecto 1, ubicado originalmente en:

`Sistema de Business Intelligence - Ferreteria/data/raw`

Archivos usados:

- `productos.csv`
- `ventas.csv`

Periodo: enero 2025 a abril 2026.

Volumen validado:

- 72 productos.
- 1,800 registros de ventas.
- 9 categorias.
- 16 periodos mensuales.

## 6. Tecnologias

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git
- GitHub
- Markdown

## 7. Roles de Trabajo

### Edelson

Responsable principal del desarrollo del proyecto.

Actividades:

- Crear estructura del proyecto.
- Ejecutar comandos.
- Escribir y probar codigo.
- Revisar resultados.
- Tomar decisiones del analisis.
- Subir el proyecto a GitHub.

### Codex

Asistente tecnico y guia del proyecto.

Actividades:

- Proponer estructura y metodologia.
- Explicar conceptos.
- Revisar codigo y documentos.
- Sugerir mejoras.
- Ayudar a resolver errores.
- Ejecutar acciones solo cuando Edelson lo pida explicitamente.

## 8. Requerimientos Funcionales

- RF01: El proyecto debe cargar los CSV originales del Proyecto 1.
- RF02: El proyecto debe validar valores nulos, duplicados y tipos de datos.
- RF03: El proyecto debe limpiar formatos de fechas, textos y columnas numericas.
- RF04: El proyecto debe generar datasets limpios.
- RF05: El proyecto debe calcular ventas totales, unidades vendidas y promedio de ventas.
- RF06: El proyecto debe identificar productos mas vendidos.
- RF07: El proyecto debe analizar tendencias de ventas por tiempo.
- RF08: El proyecto debe analizar la relacion precio vs ventas.
- RF09: El proyecto debe generar visualizaciones.
- RF10: El proyecto debe incluir conclusiones de negocio.
- RF11: El proyecto debe incluir README y documentacion.
- RF12: El proyecto debe publicarse en GitHub.

## 9. Requerimientos No Funcionales

- RNF01: El codigo debe ser claro y legible.
- RNF02: El notebook debe poder ejecutarse de principio a fin.
- RNF03: Las rutas deben estar organizadas por carpetas.
- RNF04: Los nombres de archivos deben ser descriptivos.
- RNF05: El analisis debe ser explicable para una entrevista.
- RNF06: Los resultados deben ser reproducibles.
- RNF07: El repositorio debe estar limpio y sin archivos innecesarios.
- RNF08: La documentacion debe estar escrita en lenguaje profesional.

## 10. Entregables

- `notebooks/analisis_datos_ferreteria.ipynb`
- `data/raw/productos.csv`
- `data/raw/ventas.csv`
- `data/processed/ventas_limpias.csv`
- `data/processed/productos_limpios.csv`
- `data/processed/ranking_productos.csv`
- `data/processed/resumen_categorias.csv`
- `data/processed/resumen_mensual.csv`
- `data/processed/ranking_margen_productos.csv`
- `reports/quality_report.csv`
- `reports/figures/`
- `reports/resumen_ejecutivo.json`
- `src/pipeline_analisis.py`
- `README.md`
- `docs/documento-maestro.md`
- `docs/guia-presentacion.md`
- Repositorio GitHub publicado.

## 11. Roadmap

### Fase 1 - Preparacion

- Crear estructura del proyecto.
- Crear documento maestro.
- Configurar Git y GitHub.
- Copiar dataset original del Proyecto 1.

Estado: completado.

### Fase 2 - Exploracion Inicial

- Cargar datos con Pandas.
- Revisar estructura, columnas y tipos.
- Identificar nulos, duplicados e inconsistencias.

Estado: completado.

### Fase 3 - Limpieza y Transformacion

- Normalizar columnas.
- Convertir fechas y campos numericos.
- Validar calculos de ventas.
- Unir ventas con productos.
- Crear variables derivadas.
- Generar datasets limpios.
- Generar reporte de calidad.

Estado: completado.

### Fase 4 - Analisis Descriptivo

- Calcular KPIs principales.
- Analizar productos mas vendidos.
- Analizar categorias.
- Analizar ventas por periodo.
- Analizar productos con mayor margen estimado.

Estado: completado.

### Fase 5 - Visualizacion e Insights

- Crear graficos principales.
- Interpretar patrones.
- Redactar hallazgos.
- Comparar BI vs analisis en Python.

Estado: completado.

### Fase 6 - Documentacion y GitHub

- Completar README.
- Actualizar documento maestro.
- Crear guia de presentacion.
- Revisar notebook.
- Validar entregables.
- Crear pipeline reproducible en `src/`.
- Publicar cambios en GitHub.

Estado: completado.

## 12. Criterios de Exito

El proyecto se considera terminado porque:

- El notebook contiene exploracion, limpieza, analisis, visualizaciones e insights.
- Los datasets limpios estan generados.
- Los resultados principales coinciden con el Proyecto 1.
- Existen visualizaciones claras en `reports/figures`.
- El README explica objetivo, stack, ejecucion y hallazgos.
- El repositorio esta publicado en GitHub.
- El proyecto puede explicarse en entrevista.

## 13. Diferencia Frente al Proyecto 1

El Proyecto 1 se enfoca en Business Intelligence: modelo, KPIs, Power BI y dashboard ejecutivo.

El Proyecto 2 se enfoca en analisis tecnico con Python: limpieza, validacion, transformacion, exploracion, graficos y explicacion reproducible del proceso.

## 14. Estado Actual

Estado: proyecto completo para presentacion en portafolio y entrevista.

Fases completadas:

- Fase 1: Preparacion del proyecto.
- Fase 2: Exploracion inicial del dataset.
- Fase 3: Limpieza y transformacion de datos.
- Fase 4: Analisis descriptivo.
- Fase 5: Visualizacion e insights.
- Fase 6: Cierre, documentacion final y preparacion para GitHub.

## 15. Resultados Principales

| Indicador | Resultado |
|---|---:|
| Ventas totales | S/ 128,182.96 |
| Unidades vendidas | 8,056 |
| Transacciones | 1,800 |
| Promedio de venta por linea | S/ 71.21 |
| Margen estimado | S/ 35,775.12 |
| Margen estimado % | 27.91% |

## 16. Hallazgos Principales

- Materiales de construccion es la categoria con mayor venta total.
- Cemento bolsa 42.5 kg es el producto lider por ingresos.
- Herramientas electricas tiene un ticket promedio alto y genera ingresos relevantes con pocas unidades.
- Existen productos de bajo precio con alta rotacion.
- La relacion entre precio promedio y unidades vendidas es negativa, con una correlacion aproximada de -0.3247.
- Python permitio validar y explicar tecnicamente los resultados obtenidos en el dashboard BI.

## 17. Archivos Finales del Proyecto

### Datos

- `data/raw/productos.csv`
- `data/raw/ventas.csv`
- `data/processed/productos_limpios.csv`
- `data/processed/ventas_limpias.csv`
- `data/processed/ranking_productos.csv`
- `data/processed/resumen_categorias.csv`
- `data/processed/resumen_mensual.csv`
- `data/processed/ranking_margen_productos.csv`

### Notebook

- `notebooks/analisis_datos_ferreteria.ipynb`

### Pipeline

- `src/pipeline_analisis.py`

### Reportes

- `reports/quality_report.csv`
- `reports/resumen_ejecutivo.json`
- `reports/figures/01_tendencia_mensual_ventas.png`
- `reports/figures/02_top_productos_ventas.png`
- `reports/figures/03_ventas_por_categoria.png`
- `reports/figures/04_precio_vs_unidades.png`

### Documentacion

- `README.md`
- `docs/documento-maestro.md`
- `docs/guia-presentacion.md`

## 18. Mejoras Futuras

- Agregar analisis de baja rotacion e inventario.
- Crear segmentacion de productos por ventas, margen y stock.
- Analizar estacionalidad por mes o trimestre.
- Agregar pruebas automatizadas para validar datos.
- Convertir el pipeline en paquete instalable o tarea automatizada.
