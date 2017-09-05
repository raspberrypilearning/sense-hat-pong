## Move the bat

Let's make the bat move up and down when the Sense HAT's joystick is moved.

+ In your functions section, define a new function called `move_up(event)`.

Some data called `event` will be passed to this function. The event data the function will receive is information about has happened to the Sense HAT joystick. This will include the time that the stick was used, the direction it was pushed in, and whether it was pressed, released, or held.

+ Inside the `move_up` function, add an if statement to test if the `event.action` was `'pressed'` (in other words, whether the joystick was moved).

```python
if event.action == 'pressed':
```

If the condition is met, we want the bat to move upwards. Upwards in the coordinate system on our LED screen means making the y coordinate smaller - remember that the top pixel's y coordinate is `0`.

+ If the `event.action` was `'pressed'`, take away `1` from the `bat_y` coordinate. This will allow us to redraw the bat at a different position. **Note:** because the `bat_y` variable is defined outside of this function, we also have to tell Python to use the **global** version of this variable so that we are allowed to change it from inside the function.

![Bat y moves up](images/move-bat-up.png)

Remember that just like our `draw_bat` function, this function will do nothing until it is **called**.

+ In main program section, add this line of code above the `draw_bat` function call. This line says "When the Sense HAT stick is pushed up, call the function `move_up`."

``` python
sense.stick.direction_up = move_up
```

If you run your code at this point, nothing will happen. This is because, at the moment, we are only checking for joystick movement once when the function is run. To make this function useful for our game, we need to continually check whether the joystick was moved.

+ In your main program section, put the function call to `draw_bat` inside an infinite loop.

[[[generic-python-while-true]]]

If you have used Scratch before, this should be familiar, as it is the same as using a forever loop.

![Forever loop in Scratch](images/forever-scratch.png)

+ Save and run your code. Press the joystick on the Sense HAT up (or use the arrow keys on your keyboard if you are using the emulator).

![Move the bat](images/move-the-bat.gif)

Oh dear — the result looks a bit like you are smudging the bat upwards on the screen rather than moving it! We need to clear the screen and wait a while before each time we draw the bat in the infinite loop.


+ Add this line to your infinite loop to clear the LED matrix each time before the bat is drawn.

``` python
sense.clear(0, 0, 0)
```

+ To make the program wait a little while, add a line inside the loop after `draw_bat` to `sleep` for 0.25 seconds.

[[[generic-python-sleep]]]

+ Save and run your code again. Try moving the bat and check whether it now moves up as expected.

If you move the bat too far upwards, your program tries to draw it outside the LED screen, and then the program crashes. You need to make sure that the value of the `bat_y` variable is never less than `1`, so that the bat remains on the grid at all times.

+ Add code to your `move_up` function to make sure the `bat_y` variable's value can never become smaller than `1`.

![Check bat isn't off the screen](images/check-not-off-screen.png)

+ Now follow these steps again, making a few changes to allow you to to move your bat **downwards** on the LED matrix as well as upwards.

--- hints ---
--- hint ---
Begin by writing a `move_down(event)` function containing instructions for when the bat should be moved downwards. This time, you should add `1` to `bat_y`, but only if the value of `bat_y` is less than `6`, so that the bat remains on the screen.

--- /hint ---

--- hint ---
You will need to use another line of code in your main program section to call the `move_down` function when the joystick is moved down.

``` python
sense.stick.direction_down = move_down
```

--- /hint ---

--- hint ---
Here is how your code should look:

![Moving the bat down](images/hint-move-down.png)

--- /hint ---

--- /hints ---
