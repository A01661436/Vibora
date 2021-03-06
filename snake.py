"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

import random
from turtle import *

from freegames import square, vector

#Se escogerá aleatoriamente entre estos colores
colors = ["blue", "green", "black", "yellow", "purple"]

#Elección de un color para cada elemento
theColor1 = random.choice(colors)
theColor2 = random.choice(colors)

#Posiciones iniciales de la derpiente y la comida
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#Cambia la dirección de la serpiente
def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

#Revisa que la cabeza siga dentro de la ventana
def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

#Se mueve hacia adelante un segmento
def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    #Se muere la serpiente
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    #Crece la serpiente
    if head == food:
        print('Snake:', len(snake))
        food.x = random.randrange(-15, 15) * 10
        food.y = random.randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    #El color de la serpiente
    for body in snake:
        square(body.x, body.y, 9, theColor1)

    #El color de la comida
    square(food.x, food.y, 9, theColor2)
    update()
    ontimer(move, 100)

def mover_comida():
    
    food.x = random.randrange(-15, 15) * 10
    food.y = random.randrange(-15, 15) * 10

    ontimer(mover_comida, 2000)
    

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
mover_comida()
done()
