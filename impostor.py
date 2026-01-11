import streamlit as st
import random

st.set_page_config(page_title="Juego del Impostor", page_icon="🕵️", layout="centered")

# ---------- INICIALIZAR ESTADO ----------
if "jugadores" not in st.session_state:
    st.session_state.jugadores = []
if "fase" not in st.session_state:
    st.session_state.fase = "config"
if "indice" not in st.session_state:
    st.session_state.indice = 0
if "impostores" not in st.session_state:
    st.session_state.impostores = []
if "palabra" not in st.session_state:
    st.session_state.palabra = ""

# ---------- PALABRAS ----------
PALABRAS = [
    "perro", "gato", "conejo", "caballo", "vaca", "oveja",
    "tigre", "leon", "elefante", "jirafa", "oso", "lobo",
    "manzana", "platano", "naranja", "uva", "pera", "mango",
    "mesa", "silla", "puerta", "ventana", "cama", "lampara",
    "escuela", "hospital", "mercado", "parque", "playa",
    "python", "internet", "teclado", "mouse", "pantalla",
    "futbol", "basquet", "tenis", "voleibol"
]

# ---------- CONFIGURACIÓN ----------
if st.session_state.fase == "config":
    st.title("🕵️ Juego del Impostor")

    cantidad = st.number_input(
        "Cantidad de jugadores",
        min_value=3,
        max_value=15,
        step=1
    )

    cant_impostores = st.number_input(
        "Cantidad de impostores",
        min_value=1,
        max_value=cantidad - 1,
        step=1
    )

    st.subheader("Nombres de los jugadores")

    nombres = []
    for i in range(cantidad):
        nombres.append(st.text_input(f"Jugador {i + 1}", key=f"j{i}"))

    if st.button("🎮 Iniciar juego"):
        if "" in nombres:
            st.error("❌ Todos los jugadores deben tener nombre")
        else:
            st.session_state.jugadores = nombres
            st.session_state.impostores = random.sample(nombres, cant_impostores)
            st.session_state.palabra = random.choice(PALABRAS)
            st.session_state.fase = "roles"
            st.session_state.indice = 0
            st.rerun()

# ---------- REPARTIR ROLES ----------
elif st.session_state.fase == "roles":
    jugador = st.session_state.jugadores[st.session_state.indice]

    st.title("🤫 Pantalla privada")
    st.subheader(f"Turno de: **{jugador}**")

    if st.button("👀 Ver mi rol"):
        if jugador in st.session_state.impostores:
            st.error("❌ ERES IMPOSTOR")
            st.write("🤐 No conoces la palabra")
        else:
            st.success("✅ ERES TRIPULANTE")
            st.write(f"🔑 La palabra es: **{st.session_state.palabra}**")

        st.markdown("---")

        if st.button("➡️ Pasar al siguiente"):
            st.session_state.indice += 1
            if st.session_state.indice >= len(st.session_state.jugadores):
                st.session_state.fase = "fin"
            st.rerun()

# ---------- FINAL ----------
elif st.session_state.fase == "fin":
    st.title("🎭 Roles repartidos")
    st.success("¡Que empiece el juego!")
    st.write("🗣️ Hablen, discutan y descubran a los impostores 😈")

    if st.button("🔄 Reiniciar juego"):
        st.session_state.clear()
        st.rerun()
