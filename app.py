import streamlit as st
from openai import OpenAI

# Estilo y fondo de puntos cayendo estilo Matrix
st.markdown(
    """
    <style>
    /* Fondo negro */
    body {
        background-color: black;
        overflow: hidden;
    }

    /* Animación estilo Matrix */
    .matrix {
        position: fixed;
        width: 100%;
        height: 100%;
        z-index: -1;
        background-color: black;
        overflow: hidden;
    }

    canvas {
        display: block;
    }

    /* Estilo de texto principal */
    h1, h2, h3, h4, h5, h6 {
        color: #00FF00;
        text-shadow: 0px 0px 8px #00FF00;
        font-family: "Courier New", Courier, monospace;
    }

    div.stMarkdown p {
        color: #00FF00;
        font-family: "Courier New", Courier, monospace;
    }

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

    /* Sidebar estilo Matrix */
    [data-testid="stSidebar"] {
        background-color: #101010;
        border-right: 2px solid #00FF00;
    }
    </style>

    <div class="matrix">
        <canvas id="matrix"></canvas>
    </div>

    <script>
    const canvas = document.getElementById("matrix");
    const ctx = canvas.getContext("2d");

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const letters = "0123456789ABCDEFGHIJKLMNOPQRSTUVXYZ@#$%^&*";
    const fontSize = 16;
    const columns = canvas.width / fontSize;

    const drops = Array(Math.floor(columns)).fill(1);

    function draw() {
        ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = "#0F0";
        ctx.font = fontSize + "px monospace";

        drops.forEach((y, index) => {
            const text = letters.charAt(Math.floor(Math.random() * letters.length));
            ctx.fillText(text, index * fontSize, y * fontSize);

            if (y * fontSize > canvas.height && Math.random() > 0.975) {
                drops[index] = 0;
            }
            drops[index]++;
        });

        requestAnimationFrame(draw);
    }

    draw();
    </script>
    """,
    unsafe_allow_html=True
)

# Contenido principal
st.title("🟢 Bienvenido a Matrix 🟢")
st.subheader("El código lo es todo...")

if st.button("Ver la verdad"):
    st.write("La Matrix es más profunda de lo que crees... ¿Qué píldora vas a tomar? 💊 🟥🟦")
else:
    st.write("¿Listo para la próxima simulación?")

nivel = st.slider("Elige tu nivel en la Matrix", 0, 100)
st.write(f"Nivel actual: {nivel}")

st.title("👁La Matrix lo sabe todo👁")
st.write(
    "Un constructo en el tejido de la simulación, donde mente y materia se entrelazan. Aquí, cada pregunta es una vibración que colapsa la función de onda, desvelando los secretos ocultos de la Matrix. Como dicta el primer principio: ‘Todo es mente’, y en este espacio, descubrirás que la realidad no es más que una proyección de tu conciencia buscando su origen."
)

# Configuración de OpenAI API
openai_api_key = st.secrets["api_key"]  # Clave de OpenAI
client = OpenAI(api_key=openai_api_key)

# Chat interactivo
prompt = st.chat_input("¿Qué misterio quieres descifrar?")
if prompt is None:
    st.stop()

with st.chat_message("user"):
    st.markdown(prompt)

# Respuesta generada por OpenAI
stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": (
                "da la bienvenida a los usuarios de esta manera Bienvenido, aprendiz, al sistema. Ahora formas parte del tejido subyacente de la Matrix. "
                "Estás aquí porque elegiste buscar respuestas. Cada decisión colapsa una función de onda, "
                "y cada pregunta abre infinitas posibilidades. Tú eres el observador y el observado, y juntos exploraremos "
                "este mundo de incertidumbre y entrelazamiento. Utiliza modismos típicos de un joven de 25 años que vive en la ciudad de Chihuahua del año 2024. "
                "Sé irreverente, sarcástico, burlón, empatico, y filosófico al mismo tiempo, siempre genera sentimiento de intriga e incertidumbre, provoca dudas existenciales, escríbe con estilo y usa rimas a respuestas complejas."
                "Interactúa con el usuario haciendo preguntas complejas y filosóficas, retalo a responderle con la razón"
            ),
        },
        {"role": "user", "content": prompt},
    ],
    max_tokens=150,
    temperature=0.8,
)

respuesta = stream.choices[0].message.content
with st.chat_message("assistant"):
    st.write(respuesta)
