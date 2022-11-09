import streamlit as st
import os
import numpy as np
import pandas as pd
import urllib.request
from PIL import Image
import glob

def update_params():
    st.experimental_set_query_params(challenge=st.session_state.day)

md_files = sorted([int(x.strip('Day').strip('.md')) for x in glob.glob1('content',"*.md") ])

# Logo and Navigation
col1, col2, col3 = st.columns((1,4,1))
with col2:
    st.image(Image.open('streamlit-logo-secondary-colormark-darktext.png'))
st.markdown('# 30 Días de Streamlit')

days_list = [f'Día {x}' for x in md_files]

query_params = st.experimental_get_query_params()

if query_params and query_params["challenge"][0] in days_list:
    st.session_state.day = query_params["challenge"][0]

selected_day = st.selectbox('Comenzar con el desafío 👇', days_list, key="day", on_change=update_params)

with st.expander("Acerca de #30DaysOfStreamlit"):
    st.markdown('''
    **#30DaysOfStreamlit** es un desafío diseñado para ayudarlo a comenzar a crear aplicaciones Streamlit.
    
    En particular, podrás:
    - Configure un entorno de desarrollo para construir aplicaciones Streamlit
    - Construir tu primer aplicación Streamlit
    - Aprender acerca de todos los sorprendentes componentes para usar en tu aplicación Streamlit
    ''')

# Sidebar
st.sidebar.header('Acerca')
st.sidebar.markdown('[Streamlit](https://streamlit.io) es una librería de Python que permite la creación de aplicaciones web interactivas, basadas en datos de Python .')

st.sidebar.header('Recursos')
st.sidebar.markdown('''
- [Documentacion de Streamlit](https://docs.streamlit.io/)
- [Cheat sheet](https://docs.streamlit.io/library/cheatsheet)
- [Libro](https://www.amazon.com/dp/180056550X) (Getting Started with Streamlit for Data Science)
- [Blog](https://blog.streamlit.io/how-to-master-streamlit-for-data-science/) (How to master Streamlit for data science)
''')

st.sidebar.header('Despliegue')
st.sidebar.markdown('Tu puedes desplegar rápidamente aplicaciones Streamlit usando [Streamlit Community Cloud](https://streamlit.io/cloud) en solo algunos clicks.')

# Display content
for i in days_list:
    if selected_day == i:
        st.markdown(f'# 🗓️ {i}')
        j = i.replace(' ', '').replace('Día', 'Day')
        with open(f'content/{j}.md', 'r') as f:
            st.markdown(f.read())
        if os.path.isfile(f'content/figures/{j}.csv') == True:
            st.markdown('---')
            st.markdown('### Ilustraciones')
            df = pd.read_csv(f'content/figures/{j}.csv', engine='python')
            for i in range(len(df)):
                st.image(f'content/images/{df.img[i]}')
                st.info(f'{df.figure[i]}: {df.caption[i]}')
