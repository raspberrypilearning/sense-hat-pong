from sense_hat import SenseHat
from random import choice
from copy import deepcopy
import curses


sense = SenseHat()

sense.clear(0,0,0)
mine = (80,0,0)
vide = (40,40,40,40)
marque = (255,0,0)
libre = (255,255,255)
touche = (0,0,255)
x = 0
y = 0
ratios = [mine,vide,vide,vide,vide]

tableau_original=[]
for i in range(8):
    tableau_original.append([choice(ratios) for i in range(8)]) 

tableau_jeu = deepcopy(tableau_original)

ecran = curses.initscr()
ecran.keypad(True)
curses.cbreak()
#curses.noecho()

def aplati() :
    plat = [i for j in tableau_jeu for i in j]
    return plat

def test_position(x,y):
    global jeu_termine
    if tableau_jeu[y][x] == marque:
        if tableau_original[y][x] == mine:
            ecran.addstr(12,12,'C'était une mine')
            jeu_termine = True
        if tableau_original[y][x] == vide:
            tableau_jeu[y][x] = vide
            trouve_vide(x,y)
    elif tableau_jeu[y][x] == libre:
        pass
    else:
        tableau_jeu[y][x] = marque
        ecran.addstr(12,12,'Marqué')
    
def trouve_vide(x,y):
    teste = []
    cascade = []
    cascade.append((x,y))
    while len(cascade) != 0:
        test = cascade.pop(0)
        adjacent = 0
        autour = obtenir_autour(test[0],test[1])
        adjacent, no_mines, teste = test_autour(autour,teste)
        for carre in no_mines:
            if carre not in teste:
                cascade.append(carre)
        teste.append(test)
        if adjacent == 0:
            tableau_jeu[test[1]][test[0]] = libre
        else:
            tableau_jeu[test[1]][test[0]] = touche

def obtenir_autour(x,y):
    autour = []
    for i in range(x-1,x+1):
        for j in range(y-1,y+1):
            if (i,j) != (x,y):
                autour.append((i,j))
    return autour

def test_autour(autour,teste):
    adjacent = 0
    no_mines = []
    for carre in autour:
        if carre not in teste:
            teste.append(carre)
        try:
            if tableau_original[carre[1]][carre[0]] == mine:
                adjacent += 1
            elif tableau_original[carre[1]][carre[0]] == vide:
                no_mines.append(carre)
        except IndexError:
            pass
    return adjacent, no_mines, teste
        


jeu_termine = False

while not jeu_termine:

    sense.set_pixels(aplati())
    sense.set_pixel(x,y,0,255,0)

    touche = ecran.getch()
    
    if touche == curses.KEY_LEFT:
        if x > 0:
            x -= 1

    if touche == curses.KEY_RIGHT:
        if x < 7:
            x += 1
            
    if touche == curses.KEY_UP:
        if y > 0:
            y -= 1

    if touche == curses.KEY_DOWN:
        if y < 7:
            y += 1

    if touche == ord('\n'):
        test_position(x,y)

