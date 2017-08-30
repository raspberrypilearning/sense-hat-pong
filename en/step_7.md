## Create a ball

The next step is to create the ball. But first, a little maths!

If you think about a moving ball, it has two essential properties. It has a position and a velocity (speed in a straight line). As you're only working in two dimensions, both of these properties can be described by two numbers each:

- The ball's position, like the bat, has a vertical and horizontal position.
- The ball's velocity can also be described by two numbers: how fast it's moving in the `x` dimension and how fast it's moving in the `y` dimension.

- Where you set the `y` variable near the top of your program, you can now add the ball's properties. The easiest way to store these properties is to use lists. One list can store the position and the other can store the velocity:

    ``` python
    ball_position = [3, 3]
    ball_velocity = [1, 1]
    ```

- Now you can create a function to draw the ball:

    ``` python
    def draw_ball():
    ```

- To begin with, you can add a line of code to the function to illuminate an LED. The position on the `x` axis will be the 0th item in the `ball_position` list. The `y` position will be the 1st item in the `ball_position` list. You can choose any colour you like for the ball, but in this example it's blue (`0, 0, 255`):

    ``` python
    def draw_ball():
        sense.set_pixel(ball_position[0], ball_position[1], 0, 0, 255)
    ```

- In your `while True` loop, you can now call the function:

    ``` python
    while True:
        sense.clear(0, 0, 0)
        draw_bat()
        draw_ball()
        sleep(0.25)
    ```

- Save your code by pressing `Ctrl + S` and then press `F5` to run it, and the ball should be drawn on the LED matrix.
