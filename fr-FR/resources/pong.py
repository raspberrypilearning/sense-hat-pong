from sense_hat import SenseHat
import curses
import threading
from time import sleep


##Configuer le Sense HAT
sense = SenseHat()
sense.clear(0,0,0)

## Configurer curses
ecran = curses.initscr()
ecran.keypad(True)
curses.cbreak()
curses.noecho()

##Initialise la position de la batte
y = 4

##Initialise la position de la balle
balle_position = [6,3]
balle_vitesse = [-1,-1]



def dessineraquette():
    '''Dessine la raquette en y'''
    sense.set_pixel(0,y,255,255,255)
    sense.set_pixel(0,y+1,255,255,255)
    sense.set_pixel(0,y-1,255,255,255)

def deplaceballe():
    '''Deplace et dessine la balle'''
    global jeu_termine

    while True:
        
        sleep(0.1)

        sense.set_pixel(balle_position[0],balle_position[1],0,0,0)

        balle_position[0] += balle_vitesse[0]
        balle_position[1] += balle_vitesse[1]

        if balle_position[0] == 7:
            balle_vitesse[0] = -balle_vitesse[0]

        if balle_position[1] == 0 or balle_position[1] == 7:
            balle_vitesse[1] = -balle_vitesse[1]

        if balle_position[0] == 1 and y-1 <= balle_position[1] <= y+1:
            balle_vitesse[0] = -balle_vitesse[0]

        if balle_position[0] == 0:
            break

        sense.set_pixel(balle_position[0],balle_position[1],0,0,255)

    jeu_termine = True


jeu_termine = False

thread = threading.Thread(target=deplaceballe)
thread.start()

while not jeu_termine:
    dessineraquette()
    touche = ecran.getch()
    sense.clear()

    if touche == curses.KEY_UP:
        if y > 1:
            y -= 1

    if touche == curses.KEY_DOWN:
        if y < 6:
            y += 1

sense.show_message("Perdu!", text_colour=(255,0,0))

##Nettoyer curses
ecran.keypad(0)
curses.nocbreak()
curses.echo()
curses.endwin()

