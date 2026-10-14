# Reporte de Análisis de Datos - Pandas

`Emily Barraza Machine Learning pandas, NC 0025`

## 1. DataFrame Convertido
```text
    Pelicula   Director  Duracion
0    Titanic    Cameron       195
1     Avatar    Cameron       162
2  Inception      Nolan       148
3     Matrix  Wachowski       136
4  Gladiator      Scott       155
5      Joker   Phillips       122
```

## 2.1 Primeras Filas (head)
```text
  Pelicula Director  Duracion
0  Titanic  Cameron       195
1   Avatar  Cameron       162
```

## 2.2 Últimas Filas (tail)
```text
    Pelicula  Director  Duracion
4  Gladiator     Scott       155
5      Joker  Phillips       122
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Pelicula      str
Director      str
Duracion    int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   Pelicula  6 non-null      str  
 1   Director  6 non-null      str  
 2   Duracion  6 non-null      int64
dtypes: int64(1), str(2)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Duracion'
```text
count      6.000
mean     153.000
std       24.996
min      122.000
25%      139.000
50%      151.500
75%      160.250
max      195.000
Name: Duracion, dtype: float64
```

## 4. Ordenar Ascendente por Duracion
```text
    Pelicula   Director  Duracion
5      Joker   Phillips       122
3     Matrix  Wachowski       136
2  Inception      Nolan       148
4  Gladiator      Scott       155
1     Avatar    Cameron       162
0    Titanic    Cameron       195
```

## 5. Ordenar Descendente por Duracion
```text
    Pelicula   Director  Duracion
0    Titanic    Cameron       195
1     Avatar    Cameron       162
4  Gladiator      Scott       155
2  Inception      Nolan       148
3     Matrix  Wachowski       136
5      Joker   Phillips       122
```
"Emily Barraza Machine Learning, NC 0025"