## Move the bat

- You can now tell the Raspberry Pi what you want to happen when the Sense HAT joystick is used. You can do this by using what are known as **callbacks**. When the stick is pushed up, a `move_up` function will be called. When the stick is pushed down, a `move_down` function will be called. You haven't written those functions yet, but you will do that next. Start with the `move_up` callback:

    ``` python
    sense.stick.direction_up = move_up
    ```

- Now above that line of code, you can write your function:

    ``` python
    def move_up(event)
        if event.action == 'pressed':
            y -= 1
    ```

    Did you notice the `event` parameter? When the stick is pressed, your function will be passed some information about the joystick `event`. This will include the time that the stick was used, the direction it was pushed, and whether it was pressed, released, or held.

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
