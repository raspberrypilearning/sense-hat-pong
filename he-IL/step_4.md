## Light up an LED

Games often use the coordinates `x` and `y` to determine where an object is on the display. `x` is used to set the horizontal position of an object, and `y` is used to set the vertical position of an object.

We can do the same with the LEDs on the Sense HAT.

[[[rpi-sensehat-led-coordinates]]]

Let's start our Pong game by lighting up a single LED to create a ball, and then adding a few more to create a bat.

+ Open IDLE if you are using a physical Sense HAT, or open a new trinket if you are using the [emulator](http://trinket.io/sense-hat).

[[[rpi-gui-idle-opening]]]

+ Add this code at the start of your file to import the `sense_hat` module and connect to the Sense HAT.

```python
from sense_hat import SenseHat
sense = SenseHat()
```

+ The bat will be white. Define a variable called `white`, and set its value to `(255, 255, 255)`, which is the RGB colour representation of white.

[[[rpi-sensehat-display-colour]]]

[[[generic-theory-colours]]]

The bat will always be on the far left-hand column of pixels, so its `x` value will always be `0`, but its `y` value will change as you move the bat up and down.

+ Create another variable `bat_y` and set its value to `4`.

+ Set the LED at the position `(0, bat_y)` to `white` using the `set_pixel` method.

[[[rpi-sensehat-single-pixel]]]

--- hints ---

--- hint ---

First, create a variable with the name `white` and set it equal to `(255, 255, 255)` like this:

```python
white = (255, 255, 255)
```

--- /hint ---

--- hint ---

On the next line, create another variable just like you did for the colour `white`, except this time the name will be `bat_y` and the value will be `4`.

--- /hint ---

--- hint ---

Your finished code should look like this:

```python
from sense_hat import SenseHat
sense = SenseHat()

white = (255, 255, 255)

bat_y = 4

sense.set_pixel(0, bat_y, white)
```

--- /hint---

--- /hints ---

+ Save and run your code. A single LED should now be illuminated in white on the left side of the LED matrix.

![Single LED lit](images/single-led.png)
