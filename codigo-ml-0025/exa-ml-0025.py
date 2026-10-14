# Emily Barraza Machine Learning pandas, NC 0025
import sys
import os
import io
import pandas as pd


# Ruta para importar el diccionario
ruta_datos = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "datos-de-entrada-ml-0025"
    )
)

sys.path.insert(0, ruta_datos)

import dicc_0025

print("Emily Barraza Machine Learning pandas, NC 0025")

# Lista para guardar los resultados
contenido_md = []

encabezado = "Emily Barraza Machine Learning pandas, NC 0025"

contenido_md.append(
    f"# Reporte de Análisis de Datos - Pandas\n\n"
    f"`{encabezado}`\n"
)


def registrar(titulo, contenido):
    """Muestra los resultados y los guarda en Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)

    contenido_md.append(
        f"## {titulo}\n```text\n{contenido}\n```\n"
    )


# 1. Convertir el diccionario a DataFrame
df = pd.DataFrame(dicc_0025.datos_peliculas)

registrar("1. DataFrame Convertido", df)


# 2. Información estructural

# 2.1 Primeras filas
registrar("2.1 Primeras Filas (head)", df.head(2))

# 2.2 Últimas filas
registrar("2.2 Últimas Filas (tail)", df.tail(2))

# 2.3 Dimensiones
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)

# 2.4 Tipos de datos
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# 2.5 Información general
buffer = io.StringIO()
df.info(buf=buffer)

registrar(
    "2.5 Información General (info)",
    buffer.getvalue()
)


# 3. Estadísticas de la duración de las películas
registrar(
    "3. Estadísticas Generales de la Columna 'Duracion'",
    df["Duracion"].describe()
)


# 4. Orden ascendente por duración
df_asc_duracion = df.sort_values(
    by="Duracion",
    ascending=True
)

registrar(
    "4. Ordenar Ascendente por Duracion",
    df_asc_duracion
)


# 5. Orden descendente por duración
df_desc_duracion = df.sort_values(
    by="Duracion",
    ascending=False
)

registrar(
    "5. Ordenar Descendente por Duracion",
    df_desc_duracion
)


# 6. Guardar el reporte Markdown
carpeta_resultados = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "resultados-0025"
    )
)

os.makedirs(carpeta_resultados, exist_ok=True)

ruta_archivo_md = os.path.join(
    carpeta_resultados,
    "resultados-ml-0025.md"
)

with open(ruta_archivo_md, "w", encoding="utf-8") as archivo:
    archivo.write("\n".join(contenido_md))

print(
    f"\n[ÉXITO] Archivo generado correctamente en:\n"
    f"{ruta_archivo_md}"
)
# Emily Barraza Machine Learning pandas, NC 0025
print("Emily Barraza Machine Learning pandas, NC 0025")

