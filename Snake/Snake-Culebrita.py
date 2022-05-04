# SNAKES GAME
# Use ARROW KEYS to play, SPACE BAR for pausing/resuming and Esc Key for exiting
# Juego de la culebrita
# Mover con las teclas flecha, espacio para pausar/renaudar & ESC para salir

import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

# Constantes

WINDOW_ALTO = 60
WINDOW_LARGO = 20 

# Window setup
# Ajustes de la ventana
curses.initscr()
win = curses.newwin(WINDOW_LARGO,WINDOW_ALTO,0,0) #x,y
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)#-1

# Snake & Food
# Culebra & Comida
snake = [(4,4),(4,3),(4,2)]
food = [(6,6)]

win.addch(food[0], food[1], '#')
# Game Logic
# Logica
score = 0

ESC = 27
key = curses.KEY_RIGHT


while key != ESC:
    win.addstr(0, 2, 'score ' + str(score) + ' ')
    win.timeout(150 - (len(snake)) // 5 + len(snake)//10 % 120) # increase speed/aumenta velocidad

    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    # Calculate next coordinates
    # Calcular proximas coordenadas
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    snake.insert(0, (y, x))    # appdend / metodo append 0(n)

    # Check if we hit the border
    # Checkar si chocamos en algun borde
    if y == 0: break
    if y == WINDOW_ALTO -1 : break
    if x == 0: break
    if x == WINDOW_LARGO -1 : break

    # If snake runs over itself
    # Si la culebra choca consigo misma
    if snake[0] in snake[1:]: break

    if snake [0] == food:
        # Eat food
        # Come la comida
        score += 1
        food = ()
        while food == ():
            food = (randint(1,WINDOW_ALTO-2), randint(1,WINDOW_LARGO-2))
            if food in snake:
                food = ()
                win.addch(food[0], food[1], '#')
    else:
        # Move snake
        # Mover culebra
        last = snake.pop()
        win.addch(last[0], last[1], ' ')

    win.addch(snake[0][0], snake[0][1], '*')
    #...

curses.endwin()
print (f"Final Score = {score}" )