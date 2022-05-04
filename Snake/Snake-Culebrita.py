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

# Game Logic
# Logica
score = 0

while True:
    event = win.getch()
    #...

curses.endwin()
print (f"Final Score = {score}" )