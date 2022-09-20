# st.secrets

`st.secrets` le permite almacenar información confidencial, como claves API, contraseñas de bases de datos u otras credenciales.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.secrets/)

## Código
Así es como se usa `st.secrets`:
```python
import streamlit as st

st.title('st.secrets')

st.write(st.secrets['message'])
```

## Explicación línea por línea
Lo primero que debe hacer al crear una aplicación Streamlit es comenzar importando la biblioteca `streamlit` como `st` así:
```python
import streamlit as st
```

A esto le sigue la creación de un título para la aplicación:
```python
st.title('st.secrets')
```

Finalmente, mostraremos los secretos almacenados:
```python
st.write(st.secrets['message'])
```

Cabe señalar que los secretos se pueden almacenar en Streamlit Cloud como se muestra en las capturas de pantalla que se muestran a continuación.

Si esta trabajando localmente, pueden ser almacenadas en `.streamlit/secrets.toml`, pero asegurese evitar subir esto al repositorio de GitHub. 

## Otras lecturas
- [Agregue secretos a sus aplicaciones Streamlit] (https://blog.streamlit.io/secrets-in-sharing-apps/)
- [Gestión de secretos](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)
