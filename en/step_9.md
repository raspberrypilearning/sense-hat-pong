## Collision with the bat

Now that the ball bounces 

- You can start by making the ball bounce when it gets close to the horizontal position of the bat, no matter where the bat is vertically. Add this to your `draw_ball` function:

    ``` python
    if ball_position[0] == 1:
        ball_velocity[0] = -ball_velocity[0]
    ```

- Run this code and the ball will bounce forever.

- Now the conditional needs to check the position of the bat. Switch over to the shell window to test this out:

	``` python
	>>> y = 3
	>>> 2 <= y <= 4
	```

	The interpreter is telling you that the statement you've just written is `True`. Look closely at the line. In English it would read as `Two is less than or equal to y, which is less than or equal to four.` This is a very handy way of determining if one number is between another two numbers or not.

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
