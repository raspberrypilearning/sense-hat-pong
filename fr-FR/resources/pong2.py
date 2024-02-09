from time import sleep
#from sense_hat import SenseHat
from sense_emu import SenseHat
sense = SenseHat()


sense.clear(0, 0, 0)

y = 4
balle_position=[6, 3]
balle_vitesse=[-1, -1]

def dessine_raquette():
    sense.set_pixel(0, y, 255, 255, 255)
    sense.set_pixel(0, y+1, 255, 255, 255)
    sense.set_pixel(0, y-1, 255, 255, 255)
        
def balle_joue():
    sense.set_pixel(balle_position[0], balle_position[1], 0, 0, 0)

    balle_position[0] += balle_vitesse[0]
    balle_position[1] += balle_vitesse[1]

    if balle_position[1] == 0 or balle_position[1] == 7:
        balle_vitesse[1] = -balle_vitesse[1]
    if balle_position[0] == 7:
        balle_vitesse[0] = -balle_vitesse[0]
    if balle_position[0] == 1 and y-1 <= balle_position[1] <= y+1:
        balle_vitesse[0] = -balle_vitesse[0]
    if balle_position[0] == 0:
        return False

    sense.set_pixel(balle_position[0], balle_position[1], 0, 0, 255)
    return True

def deplace_haut(event):
    global y
    if y > 1 and event.action=='pressed':
        y -= 1
    print(event)

def deplace_bas(event):
    global y
    if y < 6 and event.action=='pressed':
        y += 1
    print(event)


sense.stick.direction_up = deplace_haut
sense.stick.direction_down = deplace_bas

while balle_joue():
    dessine_raquette()
    sleep(0.25)
    sense.clear(0, 0, 0)
    
sense.show_message("Tu as perdu", text_colour=(255, 0, 0))
