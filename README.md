# Juego de Evitar Obstáculos

Este es un juego simple desarrollado en Python utilizando la biblioteca Pygame. El objetivo del juego es evitar los obstáculos que caen desde la parte superior de la pantalla durante el mayor tiempo posible para obtener la puntuación más alta.

## Cómo jugar

1. Ejecuta el script `juego_obstaculos.py` para iniciar el juego.
2. En el menú de inicio, presiona la tecla `ENTER` para comenzar a jugar.
3. Usa las teclas de flecha izquierda (`←`) y derecha (`→`) para mover al jugador y esquivar los obstáculos que caen.
4. La velocidad en la que aparecen y el número de los obstáculos aumentará progresivamente a medida que pasa el tiempo, lo que hará que el juego sea más difícil.
5. El juego termina cuando el jugador colisiona con un obstáculo.
6. El puntaje se incrementa en función del tiempo que sobrevive el jugador. ¡Intenta obtener la puntuación más alta!

## Dificultad

El juego ajusta automáticamente la dificultad para aumentar el desafío a medida que juegas:

- La velocidad de los obstáculos aumenta progresivamente, lo que requiere que el jugador reaccione más rápido.
- La velocidad con la que aparecen nuevos obstáculos también se incrementa a medida que aumenta tu puntaje.

## Menú de Inicio y Puntaje Máximo

El juego cuenta con un menú de inicio donde se muestra el puntaje máximo de la sesión de juego anterior, lo que te motivará a superar tu propio récord.

## Game Over

Cuando el jugador colisiona con un obstáculo, el juego muestra un mensaje de "Game Over" durante un breve periodo de tiempo antes de volver al menú de inicio.

## Requisitos

Para ejecutar el juego, necesitarás tener instalado Python y la biblioteca Pygame en tu sistema.

## Instalación

1. Clona o descarga este repositorio en tu computadora.
2. Asegúrate de tener Python instalado en tu sistema.
3. Instala la biblioteca Pygame con el siguiente comando:

```bash
pip install pygame
```

## Ejecución

Una vez que hayas instalado los requisitos, ejecuta el juego con el siguiente comando:

```bash
python juego_obstaculos.py
```

¡Disfruta del juego y trata de obtener la puntuación más alta!

## Créditos

Este juego fue creado por Julián Calle como parte de un proyecto de desarrollo de juegos en Python.
