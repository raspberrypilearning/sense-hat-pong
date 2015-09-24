from sense_hat import SenseHat
import threading
from time import sleep
import curses

##Set up the sense hat
sense = SenseHat()
sense.clear(0,0,0)

##initialise bat position
y = 4

##initialise ball position
ball_position = [6,3]
ball_speed = [-1,-1]

## Set up curses
screen = curses.initscr()
screen.keypad(True)
curses.cbreak()
curses.noecho()

def drawbat(y):
    '''Draw the bat about y'''
    sense.set_pixel(0,y,255,255,255)
    sense.set_pixel(0,y+1,255,255,255)
    sense.set_pixel(0,y-1,255,255,255)

def moveball():
    '''Move and draw the ball'''
    global game_over

    while True:
        
        sleep(0.1)

        sense.set_pixel(ball_position[0],ball_position[1],0,0,0)

        ball_position[0] += ball_speed[0]
        ball_position[1] += ball_speed[1]

        if ball_position[0] == 7:
            ball_speed[0] = -ball_speed[0]

        if ball_position[1] == 0 or ball_position[1] == 7:
            ball_speed[1] = -ball_speed[1]

        if ball_position[0] == 1 and y-1 <= ball_position[1] <= y+1:
            ball_speed[0] = -ball_speed[0]

        if ball_position[0] == 0:
            break

        sense.set_pixel(ball_position[0],ball_position[1],0,0,255)

    game_over = True


game_over = False

thread = threading.Thread(target=moveball)
thread.start()

while not game_over:
    drawbat(y)
    key = screen.getch()
    sense.clear()

    if key == curses.KEY_UP:
        if y > 1:
            y -= 1

    if key == curses.KEY_DOWN:
        if y < 6:
            y += 1

    screen.clear()

sense.show_message("You Lose", text_colour=(255,0,0))

##Clean up curses
screen.keypad(0)
curses.nocbreak()
curses.echo()
curses.endwin()

