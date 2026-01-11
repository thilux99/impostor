import streamlit as st
import random

st.set_page_config(page_title="Juego del Impostor", page_icon="🕵️")

st.title("🕵️ Juego del Impostor")

# ---------- ESTADO ----------
if "jugadores" not in st.session_state:
    st.session_state.jugadores = []
    st.session_state.palabra = ""
    st.session_state.impostor = ""
    st.session_state.indice = 0
    st.session_state.estado = "config"   # config | roles | fin
    st.session_state.mostrar_rol = False

# ---------- PALABRAS ----------
palabras = [
    "perro", "gato", "mesa", "silla", "lampara",
    "escuela", "hospital", "playa",
    "python", "teclado", "pantalla",
    "futbol", "tenis", "basquet"
]

# =====================================================
# PANTALLA 1: CONFIGURACIÓN
# =====================================================
if st.session_state.estado == "config":

    st.subheader("👥 Agregar jugadores (mínimo 3)")

    nombre = st.text_input("Nombre del jugador")

    if st.button("➕ Agregar jugador"):
        if nombre:
            st.session_state.jugadores.append(nombre)
            st.rerun()   # 🔥 esto “limpia” visualmente el input

    if st.session_state.jugadores:
        st.write("Jugadores:")
        for j in st.session_state.jugadores:
            st.write("•", j)

    if len(st.session_state.jugadores) >= 3:
        if st.button("🎮 Iniciar juego"):
            st.session_state.palabra = random.choice(palabras)
            st.session_state.impostor = random.choice(st.session_state.jugadores)
            st.session_state.estado = "roles"
            st.session_state.indice = 0
            st.session_state.mostrar_rol = False
            st.rerun()

# =====================================================
# PANTALLA 2: ROLES
# =====================================================
elif st.session_state.estado == "roles":

    jugador = st.session_state.jugadores[st.session_state.indice]
    st.subheader(f"Turno de: {jugador}")

    if not st.session_state.mostrar_rol:
        if st.button("👁️ Ver rol"):
            st.session_state.mostrar_rol = True
            st.rerun()
    else:
        if jugador == st.session_state.impostor:
            st.error("❌ ERES EL IMPOSTOR\n\n🤫 No conoces la palabra")
        else:
            st.success(f"✅ ERES TRIPULANTE\n\n🔑 Palabra: {st.session_state.palabra}")

        if st.button("➡️ Siguiente jugador"):
            st.session_state.mostrar_rol = False
            st.session_state.indice += 1

            if st.session_state.indice >= len(st.session_state.jugadores):
                st.session_state.estado = "fin"

            st.rerun()   # 🔥 “pantalla limpia”

# =====================================================
# PANTALLA 3: FIN
# =====================================================
elif st.session_state.estado == "fin":

    st.success("🎭 Todos los roles fueron repartidos")
    st.write("¡Ahora jueguen y descubran al impostor!")

    if st.b
