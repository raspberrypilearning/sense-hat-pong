from time import sleep
#from sense_hat import SenseHat
from sense_emu import SenseHat
sense = SenseHat()

y = 4
bal_positie = [3, 3]
bal_snelheid = [1, 1]

def teken_batje():
    sense.set_pixel(0, y, 255, 255, 255)
    sense.set_pixel(0, y+1, 255, 255, 255)
    sense.set_pixel(0, y-1, 255, 255, 255)
        
def move_up(event):
    global y
    if y > 1 and event.action=='pressed':
        y -= 1
    print(event)

def move_down(event):
    global y
    if y < 6 and event.action=='pressed':
        y += 1
    print(event)

def teken_bal():
    sense.set_pixel(bal_positie[0], bal_positie[1], 0, 0, 255)
    bal_positie[0] += bal_snelheid[0]
    bal_positie[1] += bal_snelheid[1]
    if bal_positie[0] == 7:
        bal_snelheid[0] = -bal_snelheid[0]
    if bal_positie[1] == 0 or bal_positie[1] == 7:
        bal_snelheid[1] = -bal_snelheid[1]
    if bal_positie[0] == 0:
        sense.show_message("Jij verliest", text_colour=(255, 0, 0))
        quit()
    if bal_positie[0] == 1 and y - 1 <= bal_positie[1] <= y+1:
        bal_snelheid[0] = -bal_snelheid[0]
        
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down

while True:
    sense.clear(0, 0, 0)
    teken_batje()
    teken_bal()
    sleep(0.25)
