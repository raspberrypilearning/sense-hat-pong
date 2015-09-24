# Make a Pong Clone for your Sense HAT

In this activity you will build your own Pong clone using your Raspberry Pi, a Sense HAT and some Python code.

Pong was one of the earliest graphical games ever created and was first played on an Oscilloscope.

![Oscilloscope](https://upload.wikimedia.org/wikipedia/commons/7/76/Oscilloscope.jpg)

## Writing in IDLE, but running in the terminal

Writing Python code in IDLE 3 is great because it provides colour-coded syntax highlighting, that can help you spot little mistakes that you make.

However, not all code that we write can be run from IDLE 3. Some code needs to be run from the command line.

1. Open up IDLE 3 by clicking on `Menu>Programming>Python 3 (IDLE)`
1. In IDLE 3, click on **File** and then **New File**. A text editor should open up. *This is where you will write your code*.
1. Save the blank file as `pong.py` by clicking on **File** and then **Save as...**
1. Open up a Terminal window by clicking on the icon next to the Menu.
![Terminal](images/terminal-icon.png)

## Graphics and Coordinates

When we create graphical games we often use the coordiantes `x` and `y`. `x` is used to set the horizontal position of an object. `y` is used to set the vertical position of an object.

We can do the same with the LEDs on the Sense HAT

![Coordinates](images/astro-pi-hat.png)

At the **Top-Left** corner, both x and y would have values of `0`

## Lighting up an LED

Let's start our pong game by lighting up a single LED, and then a few more to create a bat.

1. First you'll need to import the `sense_hat` library. Type the following into your `pong.py` text file.

```python
from sense_hat import SenseHat
sense = SenseHat()
```

1. The bat will always be on the far left column of pixels, so it's `x` value will be `0`, but the `y` value will change as you move the bat up and down. Start by setting the `y` value to 4, by adding this line

```python
y = 4
```

1. You can now illuminate your first LED using the following line of Python.

```python
sense.set_pixel(0,y,255,255,255)
```

1. The values `(0,y,255,255,255)` indicate the `x` and `y` position of the LED, and the colour of light it should emit. `255,255,255` is white.

1. Save you file by holding down the **Ctrl** key and then pressing the **s** key.

1. To run your file, switch over to the terminal window you opened earlier and type:

```bash
python3 pong.py
```

A single LED should now be on

![Single LED](images/single-LED.png)


##Maing a bat
1. Next we want to draw the rest of the bat, by illuminating the LED above and below the once that you currently have. To do this we're going to make a function. Select the `sense.set_pixel(0,y,255,255,255)` line and hold down **Ctrl** and then press the **x** key to cut the line. Now type the following.

```python
def drawbat():
```

1. Now paste the line you just cut into the function three times. You can do this by holding down **Ctrl** and pressing the **v** key, so that your function looks like this.

```python
def drawbat():
    sense.set_pixel(0,y,255,255,255)
    sense.set_pixel(0,y,255,255,255)
    sense.set_pixel(0,y,255,255,255)
```

1. This will try to illuminate the same pixel three times. You want the pixel above and below the `y` position to be illuminated, so edit the function to add and subtract one from `y`.

```python
def drawbat():
    sense.set_pixel(0,y,255,255,255)
    sense.set_pixel(0,y+1,255,255,255)
    sense.set_pixel(0,y-1,255,255,255)
```

1. You can test your function works by calling it on the last line of your file.

```python
drawbat()
```

1. Your entire file should so far look like this:

```python
from sense_hat import SenseHat
sense = SenseHat()

y = 4

def drawbat():
    sense.set_pixel(0,y,255,255,255)
    sense.set_pixel(0,y+1,255,255,255)
    sense.set_pixel(0,y-1,255,255,255)

drawbat()
```

1. Test your file by running it from the terminal:
```bash
python3 pong.py
```

Three LEDs should be illuminated

![Three LEDs](images/three-LED.png)

##Moving the bat
Now you have drawn a bat, you need to be able to move it using the joystick on the Sense HAT. To do this you will need the `curses` library, which makes it easy to capture keyboard input. (The joysitck is the same as the cursor keys on the keyboard.)

1. On the second line of your file, import the `curses` library, so the first two lines look like this.

```python
from sense_hat import SenseHat
import curses
```

1. Now you need to set up `curses` with a little boilerplate code. Don't worry too much about what this does. Underneath where you set up the Sense HAT, add in some extra code so that it looks like this.

```python
sense = SenseHat()
sense.clear(0,0,0)

screen = curses.initscr()
screen.keypad(True)
curses.cbreak()
curses.noecho()
```

1. Move down to the bottom of your file. We need a way to store whether the game is running or not, and then a loop to capture the joystick events. Delete the `drawbat()` line currently there and type the following:

```python
game_over = False

while not game_over:
    drawbat()

	screen.clear()

1. Run the file by typing the following into the terminal:

```bash
python3 pong.py
```

You should see the bat flickering on and off. Your terminal window might look a little strange as well. This is just curses taking over the screen. To kill the program, just click on the **X** in the top right corner of the Terminal window.

1. Now you have a loop, you can use it to find out what keys the player is pressing. To do this you store the players key press as a variable called `key` and use the `screen.getch()` to find out what is being pressed. If the player is pushing the joystick upwards, you want `y` to decrease (remember that the top left corner is 0). If the player is pulling the joystick downwards, then `y` should increase. Change your loop so it looks like this:

```python
while not game_over:
    drawbat()
    key = screen.getch()
    sense.clear()

    if key == curses.KEY_UP:
        y -= 1

    if key == curses.KEY_DOWN:
        y += 1
```

1. Open a new Terminal window and run the python code again. Try moving the joystick up and down **once** each. Now try moving the bat all the way up!

1. You probably have an error message saying that `Y position must be between 0 and 7`. This is becuase your code has tried to illuminate an LED that wasn't there. If `y` is set to `0` then the `drawbat()` function will try to illuminate the LEDs at `-1`,`0` and `1`. If `y` is `7` it will try to illuminate LEDs at `6`,`7` and `8`. As there are no LEDs at 0 or 8, this causes the program to crash. This is easy to handle though. Edit your while loop so that it looks like this.

```python
while not game_over:
    drawbat()
    key = screen.getch()
    sense.clear()

    if key == curses.KEY_UP:
        if y > 1:
            y -= 1

    if key == curses.KEY_DOWN:
        if y < 6:
            y += 1
```

Your full code should look like this:

```python
from sense_hat import SenseHat
import curses

sense = SenseHat()
sense.clear(0,0,0)

screen = curses.initscr()
screen.keypad(True)
curses.cbreak()
curses.noecho()

y = 4

def drawbat():
    sense.set_pixel(0,y,255,255,255)
    sense.set_pixel(0,y+1,255,255,255)
    sense.set_pixel(0,y-1,255,255,255)

game_over = False

while not game_over:
    drawbat()
    key = screen.getch()
    sense.clear()

    if key == curses.KEY_UP:
        if y > 1:
            y -= 1

    if key == curses.KEY_DOWN:
        if y < 6:
            y += 1

1. Try and run the code again and see if your bat moves up and down, without crashing the program. When you're happy, just close the Terminal window to kill the program.

##Bouncing a ball

1. Just like you did with the bat, you can draw a ball using a function, but first you need to give it some properties. The ball needs a starting position and a speed. You can use lists to store these numbers. Write the following two lines under the `y = 4` line in your `pong.py` file.


```python
ball_position = [6,3]
ball_speed = [-1,-1]
```

To get values out of a list, you can use the value's `index`. So if you wanted the balls horizontal position, you could type `ball_position[0]`. If you wanted the balls vertical speed, you could type `ball_speed[1]`.

1. Next you can create a function to draw and move the ball.

```python
def moveball():
    sense.set_pixel(ball_position[0],ball_position[1],0,0,0)
	ball_position[0] += ball_speed[0]
	ball_position[1] += ball_speed[1]
    sense.set_pixel(ball_position[0],ball_position[1],0,0,255)
```

This turns off the LED at the ball's position, then changes it's `x` and `y` position by it's horizontal and vertical speed. Then it illuminates the LED at the balls position in a blue colour.

1. To see the ball being drawn, you'll need to call the function. For now you can call it in the `while` loop.

```python
while not game_over:
    drawbat()
	moveball()
    key = screen.getch()
    sense.clear()

    if key == curses.KEY_UP:
        if y > 1:
            y -= 1

    if key == curses.KEY_DOWN:
        if y < 6:
            y += 1
```

1. Run your code, and expect errors. Make sure you move the joystick.

## Bouncing the ball

The first problem you should have noticed is that the ball tried to move off the LED matrix and you received the same error code as last time. This is fairly easy to fix.

1. To bounce the ball, you need to change it's speed when it gets to the edge of the LED matrix. If the speed is `-1` in the `y` direction, for instance, and the ball is at the top edge of the screen, the speed needs to become `+1`
