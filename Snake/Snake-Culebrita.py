# SNAKES GAME
# Use ARROW KEYS to play, SPACE BAR for pausing/resuming and Esc Key for exiting
# Juego de la culebrita
# Mover con las teclas flecha, espacio para pausar/renaudar & ESC para salir

import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

# Window setup
# Ajustes de la ventana
curses.initscr()
win = curses.newwin(20,60,0,0) #x,y
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)#-1

# Snake & Food
# Culebra & Comida
snake = [(4,10),(4,9),(4,8)]
food = [(10,20)]


# Game Logic
# Logica
score = 0

ESC = 27
key = curses.KEY_RIGHT


while KEY != ESC:
    win.addstr(0, 2, 'score ' + str(score) + ' ')
    win.timeout(150 - (len(snake)) // 5 + len(snake)//10 % 120) # increase speed/aumenta velocidad

    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    for c in snake:
        win.addch(c[0], c[1], '*')
    win.addch(food[0], food[1], '#')
    #...

curses.endwin()
print (f"Final Score = {score}" )