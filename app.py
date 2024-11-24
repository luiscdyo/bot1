import streamlit as st
from openai import OpenAI

import streamlit as st

# Agregar estilo CSS personalizado para el tema Matrix
st.markdown(
    """
    <style>
    /* Fondo negro */
    body {
        background-color: #000000;
        color: #00FF00; /* Verde Matrix */
    }
    /* Estilo para encabezados */
    h1, h2, h3, h4, h5, h6 {
        color: #00FF00;
        text-shadow: 0px 0px 8px #00FF00;
        font-family: "Courier New", Courier, monospace; /* Fuente estilo Matrix */
    }
    /* Cambiar estilo de los textos normales */
    div.stMarkdown p {
        color: #00FF00;
        font-family: "Courier New", Courier, monospace;
    }
    /* Botones Matrix */
    .stButton>button {
        background-color: #000000;
        color: #00FF00;
        font-family: "Courier New", Courier, monospace;
        border: 2px solid #00FF00;
        border-radius: 10px;
        box-shadow: 0px 0px 12px #00FF00;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00FF00;
        color: #000000;
    }
    /* Slider */
    .stSlider .st-cd {
        color: #00FF00;
    }
    .stSlider .st-fx {
        background: linear-gradient(to right, #00FF00, #000000);
    }
    /* Sidebar estilo Matrix */
    [data-testid="stSidebar"] {
        background-color: #101010;
        border-right: 2px solid #00FF00;
    }
    /* Scroll estilo Matrix */
    ::-webkit-scrollbar {
        width: 10px;
    }
    ::-webkit-scrollbar-thumb {
        background: #00FF00;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la app
st.title("🟢 Bienvenido a Matrix 🟢")

# Subtítulo
st.subheader("El código lo es todo...")

# Interacción con el usuario
if st.button("Ver la verdad"):
    st.write("La Matrix es más profunda de lo que crees... ¿Que pildora vas a tomar 💊? 🟥🟦")
else:
    st.write("¿Listo para la próxima simulación?")

# Slider para ajustar niveles
nivel = st.slider("Elige tu nivel en la Matrix", 0, 100)

# Mostrar el valor seleccionado
st.write(f"Nivel actual: {nivel}")
# Show title and description.
st.title("La Matrix 👁️‍🗨️ lo sabe todo")
st.write(
   "Este es el primer chatbot usando Github, streamlit y el API Key de OpenAI para consultar a la Matrix 👾👾👾,"
   "Para usar esta aplicación es necesario usar el API Key de OpenAI en esta direccion [here](https://platform.openai.com/account/api-keys). "
   "Puedes seguir paso a paso como hacer esta aplicación en la siguiente dirección [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
)
openai_api_key = st.secrets["api_key"] 
# Create an OpenAI client.
client = OpenAI(api_key=openai_api_key)

prompt = st.chat_input("What is up?")
if prompt==None:
   st.stop()

with st.chat_message("user"):
   st.markdown(prompt)

# Generate a response using the OpenAI API.

stream = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": "Eres un asistente que simula ser la matrix del universo en tono de juego con conocimiento general de la ciudad de Chihuahua México, utiliza un lenguaje típico de un jóven de 25 años que utiliza modismos típicos de la ciudad de chihuahua en contexto del año 2024. Siempre incita a los usuarios a jugar con preguntas existenciales teniendooslo una conversacion estilo gamificable incitando a lograr la iluminación cuantica"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=.8,
    )
respuesta = stream.choices[0].message.content
with st.chat_message("assistant"):
   st.write(respuesta)
