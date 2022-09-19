# st.button

`st.button` permite mostrar un boton.

## Que estamos construyendo?

Una simple aplicacion que imprime condicionalmente diferentes mensajes dependiendo si el boton fue presionado o no.


Comportamiento de la aplicacion:

1. Por defecto, la aplicacion imprime `Goodbye`
2. Una vez que se hace click sobre el boton, la aplicacion imprime `Why hello there`

## Demo app

La aplicacion de Streamlit deberia verse como la mostrada en el siguiente link:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.button/)

## Codigo

Aqui tenemos el codigo para implementar la aplicacion previamente mencionada:

```python
import streamlit as st

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

## Explicacion linea por linea


Lo primero que tenemos que hacer cuando creamos una aplicacion de Streamlit es comenzar importando la libreria `streamlit` de la siguiente manera:

```python
import streamlit as st
```

Seguimos por crear un encabezado de texto para la aplicacion:

```python
st.header('st.button')
```

Siguiente, vamos a usar los condicionales `if` y `else` para imprimir los correspondientes mensajes.

```python
if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
```

Como podemos ver en el anterior codigo, el comando `st.button()` admite el argumento `label` con el valor `Say hello`, el cual es el texto que el boton muestra.

El comando `st.write` es usado para imprimir mensajes tales como `Why hello there` o `Goodbye` dependiendo si el boton fue presionado o no, lo cual es implementado de la siguiente manera:


```python
st.write('Why hello there')
```

y

```python
st.write('Goodbye')
```

Es importante tener en cuenta que los `st.write` estan colocados debajo de las condiciones `if` y `else` para realizer el mencionado proceso de mostrar mensajes alternativos.

## Siguientes pasos

Ahora que has creado la app localmente, es hora de desplegarla en [Streamlit Cloud](https://streamlit.io/cloud) como lo vamos a mencionar proximamente en un proximo desafio.

Como esta es la primer semana de tu desafio, nosotros proveemos el codigo completo (como es mostrado en el codigo anterior) y la solucion (la app de ejemplo) dentro de esta web.

Avanzando en el proximo desafio, es recomendable que intentes implementar la Streamlit app por vos mismo.

No te preocupes si te trabas, tu siempre puedes tomar un vistazo a la solucion. 

## Referencias

Lee acerca [`st.button`](https://docs.streamlit.io/library/api-reference/widgets/st.button) en la documentacion de Streamlit.
