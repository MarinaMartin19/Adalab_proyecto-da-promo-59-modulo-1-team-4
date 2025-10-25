# Proyecto_Modulo1
Proyecto Modulo 1 donde desarrollaremos 3 juegos: Piedra, papel y tijera; El ahorcado; Preguntas y respuestas

# 🎮 Piedra, Papel o Tijera

Un juego clásico de Piedra, Papel o Tijera implementado en Python donde juegas contra la computadora.

## 📋 Descripción

Este es un juego interactivo por consola donde compites contra la computadora en el clásico juego de Piedra, Papel o Tijera. El primero en alcanzar **5 puntos** gana la partida.

## ✨ Características

- 🤖 Juega contra la computadora
- 🔒 Entrada oculta usando `getpass` para mantener tu elección secreta
- 🎯 Sistema de puntuación hasta 5 puntos
- ✅ Validación de entradas del usuario
- 📊 Marcador actualizado después de cada ronda
- 🛑 Opción de salir en cualquier momento

## 🎯 Reglas del Juego

- **Piedra** gana a **Tijera** 💎✂️
- **Papel** gana a **Piedra** 📄💎
- **Tijera** gana a **Papel** ✂️📄
- El primer jugador en alcanzar **5 puntos** gana el juego

## 🚀 Requisitos

- Python 3.x
- Módulos estándar de Python:
  - `getpass`
  - `random`

## 📦 Instalación

1. Clona o descarga el archivo del juego
2. No necesitas instalar dependencias adicionales

## ▶️ Cómo Jugar

1. Ejecuta el script:
```bash
python piedra_papel_tijera.py
```

2. Ingresa tu nombre cuando te lo pida

3. En cada ronda:
   - Escribe tu elección: `piedra`, `papel` o `tijera`
   - Tu elección no será visible en pantalla (entrada oculta)
   - La computadora hará su elección aleatoriamente
   - Se revelarán ambas elecciones
   - Se mostrará el ganador de la ronda y el marcador

4. Después de cada ronda:
   - Puedes elegir continuar (`si`) o salir (`no`)

5. El juego termina cuando:
   - Alguien alcanza 5 puntos
   - Eliges salir del juego

## 🎮 Ejemplo de Uso

```
==================================================
🎮 BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERA 🎮
==================================================

👤 Tu nombre: Leire

¡Bienvenido/a Leire!
🤖 Jugarás contra la COMPUTADORA
🎯 ¡El primero en llegar a 5 puntos GANA!

==================================================
NUEVA RONDA
==================================================

Leire, es tu turno:
⚠️ Tu elección NO se verá en pantalla (es secreta)
Elige (piedra/papel/tijera): ********
✅ Leire ya eligió su jugada
✅ La computadora ya eligió su jugada

🔓 REVELANDO ELECCIONES...

🎮 Leire eligió: PIEDRA
🤖 Computadora eligió: TIJERA

🎉 ¡Ana GANA esta ronda!
💎 La piedra rompe las tijeras

--------------------------------------------------
📊 MARCADOR:
  Leire: 1 punto(s)
  Computadora: 0 punto(s)
  🎯 Objetivo: 5 puntos
--------------------------------------------------

¿Quieres jugar otra ronda? (si/no): si
```

## 📝 Funciones Principales

- `obtener_eleccion_jugador()`: Obtiene y valida la elección del jugador
- `jugar_piedra_papel_tijera()`: Función principal que ejecuta el juego

## 🤝 Contribuciones

Este es un proyecto educativo. Si tienes sugerencias de mejora, ¡son bienvenidas!

## 📄 Licencia

Proyecto de código abierto para fines educativos.

## 👨‍💻 Autor

Proyecto creado como ejercicio de programación por le grupo 4 de la promoción 59 de ADALAB.

---

¡Disfruta del juego! 🎉