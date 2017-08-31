## Collision with the bat

Now that the ball bounces in both directions, let's make it bounce off the bat.

The bat is always situated in the far left column of the LED grid, so its `x` coordinate is always `0`.

The ball will bounce off the bat if the ball's `x` position is equal to `1` - i.e. it is in the row next to the bat.

+ Add this code to the end of the `draw_ball` function:

``` python
if ball_position[0] == 1:
    ball_velocity[0] = -ball_velocity[0]
```
This code will cause the ball to reverse direction if it reaches an `x` coordinate of `1` - but this happens regardless of whether the bat is there or not!

- Add to the condition to require the ball's `y` position to also (**and**) be anywhere between the top and bottom of the bat.

Remember that the bat is made up of 3 pixels, so this means the `y` coordinate of the ball can be anywhere **between** the top of the bat (`bat_y - 1`) and the bottom of the bat (`bat_y + 1`).

--- hints ---
--- hint ---
Add your extra condition at the location highlighted blue:

![Has it hit the bat?](images/hint-add-hit-bat.png)
--- /hint ---

--- hint ---
To check whether a value is between two values, we can write a condition like this:

```python
1 <= x <= 10
```

This condition checks whether `x` is between 1 and 10 (inclusive) by asking first whether 1 is less than or equal to x, and then whether x is less than or equal to 10. Use this to determine whether your ball's `y` coordinate is between (`bat_y - 1`) and (`bat_y + 1`).
--- /hint ---
--- hint ---
Here is how your finished code should look. The bit you should add is highlighted in blue:
![Has it hit the bat?](images/hint-add-hit-bat-solution.png)
--- /hint ---

--- /hints ---


- So to see if the ball is going to hit the bat, you can test whether the top of the bat (`y - 1`) is less than or equal to the ball's position (`ball_position[1]`), and the ball's position is less than the bottom edge of the bat (`y + 1`):

    ``` python
    if ball_position[0] == 1 and y - 1 <= ball_position[1] <= y + 1:
        ball_velocity[0] = -ball_velocity[0]
    ```

- Run your code and have a go at playing your own version of Pong.

- If you get an error, then check your code against this full listing:

    ``` python
    from time import sleep
    #from sense_hat import SenseHat
    from sense_emu import SenseHat
    sense = SenseHat()

    y = 4
    ball_position = [3, 3]
    ball_velocity = [1, 1]

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

    def draw_ball():
        sense.set_pixel(ball_position[0], ball_position[1], 0, 0, 255)
        ball_position[0] += ball_velocity[0]
        ball_position[1] += ball_velocity[1]
        if ball_position[0] == 7:
            ball_velocity[0] = -ball_velocity[0]
        if ball_position[1] == 0 or ball_position[1] == 7:
            ball_velocity[1] = -ball_velocity[1]
        if ball_position[0] == 0:
            sense.show_message("You Lose", text_colour=(255, 0, 0))
            quit()
        if ball_position[0] == 1 and y - 1 <= ball_position[1] <= y+1:
            ball_velocity[0] = -ball_velocity[0]

    sense.stick.direction_up = move_up
    sense.stick.direction_down = move_down

    while True:
        sense.clear(0, 0, 0)
        draw_bat()
        draw_ball()
        sleep(0.25)
    ```
