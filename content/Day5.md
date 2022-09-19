# st.write

`st.write` permite imprimir texto y datos en la Streamlit app. 

Además de poder mostrar texto, también se puede mostrar lo siguiente mediante el comando `st.write()`:


- Muestra cadenas; funciona como `st.markdown()`
- Muestra un `dict` de Python
- Muestra `pandas` DataFrame se puede mostrar como una tabla
- Graficos/Esquemas/Representaciones de `matplotlib`, `plotly`, `altair`, `graphviz`, `bokeh`
- Y mas (ver [st.write en la documentacion de Streamlit](https://docs.streamlit.io/library/api-reference/write-magic/st.write))

## Que estamos construyendo?

Una aplicación sencilla que muestra las diversas formas de utilizar el comando `st.write()` para mostrar texto, números, marcos de datos y gráficos.

## Demo app

La aplicacion de Streamlit deberia verse como la mostrada en el siguiente link:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.write/)

## Codigo

Así es como se usa st.write:

```python
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
```

## Explicacion linea por linea

Lo primero que tenemos que hacer cuando creamos una aplicacion de Streamlit es comenzar importando la libreria `streamlit` de la siguiente manera:

```python
import streamlit as st
```

Seguimos por crear un encabezado de texto para la aplicacion:

```python
st.header('st.write')
```

**Example 1**
Su caso de uso básico es mostrar texto y texto con formato Markdown:

```python
st.write('Hello, *World!* :sunglasses:')
```

**Example 2**
Como se mencionó anteriormente, también se puede usar para mostrar otros formatos de datos, como números:

```python
st.write(1234)
```

**Example 3**
Los DataFrames también se pueden mostrar de la siguiente manera:

```python
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)
```

**Example 4**
Puedes pasar multiples argumentos:

```python
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
```

**Example 5**
Finalmente, también puede mostrar gráficos pasándolos a una variable de la siguiente manera:

```python
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
```

## Demo app

La aplicacion de Streamlit deberia verse como la mostrada en el siguiente link:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.write/)

## Siguientes pasos

Ahora que has creado la app localmente, es hora de desplegarla en [Streamlit Cloud](https://streamlit.io/cloud) como lo vamos a mencionar proximamente en un proximo desafio.

Como esta es la primer semana de tu desafio, nosotros proveemos el codigo completo (como es mostrado en el codigo anterior) y la solucion (la app de ejemplo) dentro de esta web.

Avanzando en el proximo desafio, es recomendable que intentes implementar la Streamlit app por vos mismo.

No te preocupes si te trabas, tu siempre puedes tomar un vistazo a la solucion.

## Otras lecturas

A demas de [`st.write`](https://docs.streamlit.io/library/api-reference/write-magic/st.write), puedes explorar otras manera para mostrar texto:

- [`st.markdown`](https://docs.streamlit.io/library/api-reference/text/st.markdown)
- [`st.header`](https://docs.streamlit.io/library/api-reference/text/st.header)
- [`st.subheader`](https://docs.streamlit.io/library/api-reference/text/st.subheader)
- [`st.caption`](https://docs.streamlit.io/library/api-reference/text/st.caption)
- [`st.text`](https://docs.streamlit.io/library/api-reference/text/st.text)
- [`st.latex`](https://docs.streamlit.io/library/api-reference/text/st.latex)
- [`st.code`](https://docs.streamlit.io/library/api-reference/text/st.code)
