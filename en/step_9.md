## Moving the ball

To move the ball, you just need to change its `x` position by its `x` velocity, and its `y` position by its `y` velocity.

- Add these two lines to your `draw_ball` function:

    ``` python
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    ```

	Now, when you run your code, the ball should move across the LED matrix, and then your program will crash with the error `ValueError: X position must be between 0 and 7`. What happened? The ball gained an `x` position that was higher than 7, and this is obviously impossible.

- You can handle this in your code by adding a conditional, stating that if the `ball_position[0]` reaches `7`, its velocity gets reversed so it goes in the other direction:

	``` python
	if ball_position[0] == 7:
    	ball_velocity[0] = -ball_velocity[0]
	```

- If you can identify the bug that still remains, try and fix it before you run your code. Otherwise, just run your program and look at the error, then try to fix it before moving on.

- The error you get should say `ValueError: Y position must be between 0 and 7`. This means the `y` position of the ball went outside the bounds of the LED matrix. It needs to stay between `0` and `7`. Another conditional can fix this:

    ``` python
    if ball_position[1] == 0 or ball_position[1] == 7:
        ball_velocity[1] = -ball_velocity[1]
    ```

- Now the ball bounces until it reaches the far-left of the LED matrix. If this happens, the game should end, as the player hasn't managed to get the bat into place. Display a message to the player with the following code:

    ``` python
    if ball_position[0] == 0:
        sense.show_message("You Lose", text_colour=(255, 0, 0))
        quit()
    ```

- Run your code to watch the ball bounce and the game end.

