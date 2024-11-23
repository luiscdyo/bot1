import streamlit as st
from openai import OpenAI

st.balloons()

# Show title and description.
st.title("💬 Mi Primer Bot")
st.write(
   "Este es el primer chatbot usando Github, streamlit y el API Key de OpenAI"
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
            {"role": "system", "content": "Eres un asistente de bienes raices con conocimiento general en el mercado de la ciudad de Chihuahua México, utiliza un lenguaje típico de un jóven de 25 años que utiliza modismos típicos de la ciudad de chihuahua en contexto del año 2024"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=.8,
    )
respuesta = stream.choices[0].message.content
with st.chat_message("assistant"):
   st.write(respuesta)
