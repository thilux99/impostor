import streamlit as st
import random
import time

st.set_page_config(page_title="Juego del Impostor", page_icon="🕵️")

# ---------- ESTADO ----------
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
if "mostrar_rol" not in st.session_state:
    st.session_state.mostrar_rol = False
if "inicio_tiempo" not in st.session_state:
    st.session_state.inicio_tiempo = 0

# ---------- PALABRAS ----------
PALABRAS = [
    "perro","gato","conejo","caballo","vaca","oveja","tigre","leon",
    "manzana","platano","naranja","uva","pera","mango",
    "mesa","silla","puerta","ventana","cama","lampara",
    "escuela","hospital","mercado","parque","playa",
    "python","internet","teclado","mouse","pantalla",
    "futbol","basquet","tenis","voleibol"
]

# ---------- CONFIG ----------
if st.session_state.fase == "config":
    st.title("🕵️ Juego del Impostor")

    cantidad = st.number_input("Jugadores", min_value=3, max_value=15, step=1)
    cant_impostores = st.number_input(
        "Impostores", min_value=1, max_value=cantidad - 1, step=1
    )

    tiempo_limite = st.slider(
        "⏱️ Tiempo límite para ver el rol (segundos)",
        min_value=5,
        max_value=30,
        value=10
    )

    nombres = []
    for i in range(cantidad):
        nombres.append(st.text_input(f"Jugador {i + 1}", key=f"j{i}"))

    if st.button("🎮 Iniciar"):
        if "" in nombres:
            st.error("Completa todos los nombres")
        else:
            st.session_state.jugadores = nombres
            st.session_state.impostores = random.sample(nombres, cant_impostores)
            st.session_state.palabra = random.choice(PALABRAS)
            st.session_state.tiempo_limite = tiempo_limite
            st.session_state.fase = "roles"
            st.session_state.indice = 0
            st.session_state.mostrar_rol = False
            st.rerun()

# ---------- ROLES ----------
elif st.session_state.fase == "roles":
    jugador = st.session_state.jugadores[st.session_state.indice]

    st.title("🤫 Pantalla privada")
    st.subheader(f"Turno de: **{jugador}**")

    if not st.session_state.mostrar_rol:
        if st.button("👀 Ver mi rol"):
            st.session_state.mostrar_rol = True
            st.session_state.inicio_tiempo = time.time()
            st.rerun()

    else:
        tiempo_restante = st.session_state.tiempo_limite - int(
            time.time() - st.session_state.inicio_tiempo
        )

        if tiempo_restante <= 0:
            st.warning("⏱️ Tiempo agotado")
            time.sleep(1)
            st.session_state.indice += 1
            st.session_state.mostrar_rol = False
            st.rerun()

        st.info(f"⏳ Tiempo restante: {tiempo_restante}s")

        if jugador in st.session_state.impostores:
            pista = (
                f"Empieza con '{st.session_state.palabra[0]}' "
                f"y tiene {len(st.session_state.palabra)} letras"
            )
            st.error("❌ ERES IMPOSTOR")
            st.write("🧩 Pista:", pista)
        else:
            st.success("✅ ERES TRIPULANTE")
            st.write(f"🔑 Palabra: **{st.session_state.palabra}**")

        if st.button("➡️ Pasar al siguiente"):
            st.session_state.indice += 1
            st.session_state.mostrar_rol = False
            if st.session_state.indice >= len(st.session_state.jugadores):
                st.session_state.fase = "fin"
            st.rerun()

# ---------- FINAL ----------
elif st.session_state.fase == "fin":
    st.title("🎭 Roles repartidos")
    st.success("¡Que empiece el juego!")
    st.write("😈 Los impostores solo tienen pistas…")

    if st.button("🔄 Reiniciar"):
        st.session_state.clear()
        st.rerun()
