import streamlit as st
import random
import os

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

print("🕵️ JUEGO DEL IMPOSTOR 🔍")

# ----- Jugadores -----
jugadores = []

cantidad = int(input("¿Cuántos jugadores? (mínimo 3): "))
while cantidad < 3:
    cantidad = int(input("Debe haber al menos 3 jugadores. Intenta otra vez: "))

for i in range(cantidad):
    nombre = input(f"Nombre del jugador {i + 1}: ")
    jugadores.append(nombre)

# ----- Palabras -----
palabras = [
    "perro", "gato", "conejo", "caballo", "vaca", "oveja",
    "tigre", "leon", "elefante", "jirafa", "oso", "lobo",
    "delfin", "ballena", "tiburon", "serpiente", "tortuga",
    "manzana", "platano", "naranja", "uva", "pera", "mango",
    "fresa", "sandia", "melon", "limon", "piña",
    "mesa", "silla", "puerta", "ventana", "cama", "lampara",
    "reloj", "mochila", "botella", "telefono", "computadora",
    "escuela", "hospital", "mercado", "parque", "playa",
    "montaña", "bosque", "ciudad", "biblioteca",
    "python", "internet", "teclado", "mouse", "pantalla",
    "programacion", "codigo", "software", "hardware",
    "futbol", "basquet", "tenis", "voleibol",
    "natacion", "boxeo", "ciclismo"
]

palabra_secreta = random.choice(palabras)

# ----- Impostor -----
impostor = random.choice(jugadores)

# ----- Repartir roles -----
for jugador in jugadores:
    limpiar()
    print(f"Turno de: {jugador}")
    input("Presiona ENTER para ver tu rol...")

    if jugador == impostor:
        print("\n❌ ERES EL IMPOSTOR")
        print("🤫 No conoces la palabra")
    else:
        print("\n✅ ERES TRIPULANTE")
        print("🔑 La palabra secreta es:", palabra_secreta)

    input("\nPresiona ENTER y pasa la pantalla...")

# ----- Fin -----
limpiar()
print("🎭 Todos los roles fueron repartidos")
print("¡Empieza el juego!")
