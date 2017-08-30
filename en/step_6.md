## Move the bat

Let's make the bat move up and down when the joystick on the Sense HAT is moved.

+ In your functions section, start a new function called `move_up(event)`.

This function will be passed some data called `event`. The event data it will receive is what has happened to the Sense HAT joystick. This will include the time that the stick was used, the direction it was pushed, and whether it was pressed, released, or held.

+ Inside the function, add an `if` statement to test if the `event.action` was 'pressed', or in other words the joystick was moved.

```python
if event.action == 'pressed':
```

If the condition is met, we want the bat to move up. Upwards on our coordinates means making the number smaller - remember that the top pixel is 0.

+ If the `event.action` was 'pressed', take away 1 from the `bat_y` coordinate. Because the `bat_y` variable is defined outside of this function, we also have to tell Python to use the **global** version of this variable so that we are allowed to change it from inside the function.

![Bat y moves up](images/move-bat-up.png)

Remember that just like our `draw_bat` function, this function will do nothing until it is **called**.

+ At the bottom of the main program section, add this line of code to say _"When the Sense HAT stick is pushed up, call the function `move_up`."_

``` python
sense.stick.direction_up = move_up
```

If you run your code at this point, nothing will happen. This is because we need to continually check whether the player has moved the joystick, rather than only checking once when the program is run.

+ Put the two lines of code in your main program section inside an infinite loop

[[[generic-python-while-true]]]

If you have used Scratch before, this should be familiar as it is the same as a forever loop

![Forever loop in Scratch](images/forever-scratch.png)

+ Save and run your code. Press the joystick on the Sense HAT up (or use the arrow keys on your keyboard if you are using the emulator).


- To test out the code, you can draw the bat and clear the screen in a infinite loop. Add this to the bottom of your code:

    ``` python
    while True:
        sense.clear(0, 0, 0)
        draw_bat()
        sleep(0.25)
    ```

- Does anything happen when you run the file and use the joystick? Probably not. This is because the variable `y` is a **global variable**. Variables outside of a function can't be changed by that function, unless you tell Python it's a global variable. Change your `move_up` function so it reads like this:

    ``` python
    def move_up(event)
        global y
        if event.action == 'pressed':
            y -= 1
    ```

    Now save and run your code, and you should be able to move the bat. There should be a bug in your code, though: can you spot it?

- If you move the bat too far up, your program tries to draw the bat off the LED grid. You need to check that the `y` variable never goes lower than `1`, with the following code:

    ``` python
    def move_up(event)
        global y
        if event.action == 'pressed' and y > 1:
            y -= 1
    ```

	Running this code and moving the joystick up should move the bat.

- Next, you need to be able to move your bat down. Start by using a callback, just like you did before. Add this next line:

    ``` python
    sense.stick.direction_down = move_down
    ```

- Now you need a `move_down` function. Make sure this goes above your callback lines:

    ``` python
    def move_down():
    ```

- Can you figure out the rest of the code for this function yourself?
    - You'll need a declaration that `y` is a `global` variable.
    - You'll need the `y` variable to change by `+1`, but only if the action is `pressed` and `y < 7`.

Your complete code should now look something like this:

``` python
from time import sleep
#from sense_hat import SenseHat
from sense_emu import SenseHat
sense = SenseHat()

y = 4

def draw_bat():
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

sense.stick.direction_up = move_up
sense.stick.direction_down = move_down

while True:
	sense.clear(0, 0, 0)
        draw_bat()
        sleep(0.25)
```
