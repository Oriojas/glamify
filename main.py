import pandas
import pandas as pd

import openai_con
import prodia_con
import streamlit as st
from time import sleep

st.set_page_config(page_title="Glamify",
                   page_icon="💄",
                   layout="wide")

delay = 10
list_url = []

st.header('💄 Glamify', divider='rainbow')
st.markdown("Una aplicación que te hace lucir glamorosa, usando inteligencia artificial"
            " para producir imágenes espectaculares y recomendaciones de estilos de maquillaje.")

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Crea tu mejor maquillaje")
        piel = st.text_input("Tu color de piel:", "oscura")
        ojos = st.text_input("Tu color de ojos:", "cafes")
        ocasion = st.text_input("Que ocasión:", "fiesta elegante")
        cabello = st.text_input("Color cabello:", "oscuro")
        color_m = st.text_input("Color principal", "azul")
        cara_opt = st.selectbox("Forma cara",
                                ("redonda", "afilada", "normal", "cuadrada"))
        t_maquillaje = st.selectbox("Tipo maquillaje",
                                    ("discreto", "vistoso", "fantasia", "elegante"))

        st.markdown("Prueba las veces que quieras hasta crear tu estilo propio, en la parte inferior te mostraremos dos"
                    " posibilidades para que escojas, solo oprime el boton con la alternativa que te sientas"
                    " mas comod@ 👇🏼 ")

        init_prompt = "Crea una cara con lindo maquillaje para una persona que asiste a una"

        init_prompt = (f"{init_prompt} {ocasion}, tiene la piel {piel}, los ojos {ojos}, el cabello {cabello}, "
                       f"la cara {cara_opt}, el maquillaje {color_m}"
                       f" , de tipo {t_maquillaje} y con el rostro de frente")

        col11, col12 = st.columns(2)

        with col11:
            st.markdown("")
            st.markdown("")
            send = st.button("generar", type="secondary")
        with col12:
            st.markdown(### Colocar algo)

        if send:
            # st.markdown(f"### {init_prompt}")
            response_trans = openai_con.translate(prompt=init_prompt)

            # st.markdown(f"### {response_trans}")

            for i in list(range(2)):
                prodia_obj = prodia_con.Prodia()
                response_dict = prodia_obj.create(prompt=response_trans)
                img_job = dict(eval(response_dict)).get("job")

                sleep(delay)

                response_img = prodia_obj.download(n_job=img_job)
                response_url_img = dict(eval(response_img.text)).get("imageUrl")

                list_url.append(response_url_img)

    with col2:
        st.markdown("### Prueba muchas combinaciones")
        with st.container():
            col1, col2 = st.columns(2)

            if len(list_url) == 0:
                with col1:
                    st.image("img/img_1.png")

                with col2:
                    st.image("img/img_3.png")

            else:
                with col1:
                    st.image(list_url[0])

                with col2:
                    st.image(list_url[1])

                df = pd.read_csv("table.csv", index_col=0)
                st.dataframe(df)

                st.button("👩🏼‍ contactar tu consultora", type="primary")

            st.success('Listo!')

