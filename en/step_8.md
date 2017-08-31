## Move the ball

To get the ball moving, you need to change its `x` position by its `x` velocity, and its `y` position by its `y` velocity.

The first coordinate in each list you just created represents the ball's `x` property - so `ball_position[0]` is the current `x` coordinate and `ball_velocity[0]` is how fast it should move in the `x` direction.

+ Inside your `draw_ball` function, add this line of code to add the ball's velocity (currently 1) to the ball's current position in the `x` direction.

``` python
ball_position[0] += ball_velocity[0]
```

![Velocity x](images/velocity-x.png)

+ Save and run your code. The ball will move across the screen until it reaches the edge, and then the program will crash. Why do you think this happens?

--- collapse ---
---
title: Answer
---
You've seen this error before when you made the paddle. The ball moves across the LED matrix and then the program crashes with the error `ValueError: X position must be between 0 and 7`.

The ball moved to an `x` position that was higher than 7, which was off the end of the LED matrix.
--- /collapse ---

+ Add a conditional, stating that if the `ball_position[0]` reaches `7`, its velocity gets reversed so it goes in the other direction:

``` python
if ball_position[0] == 7:
	ball_velocity[0] = -ball_velocity[0]
```

+ Save and run your code again. The ball should bounce off the right edge of the matrix, but when it reaches the left edge, you'll get another error.

+ Add to the conditional to say that the ball should reverse direction if it's position is equal to 7 OR is equal to 0.

--- hints ---
--- hint ---
Add your extra condition at the point highlighted in blue:

![Add to conditional](images/add-to-conditional.png)
--- /hint ---

--- hint ---
Here is how your code should look:
``` python
if ball_position[1] == 0 or ball_position[1] == 7:
    ball_velocity[1] = -ball_velocity[1]
```
--- /hint ---
--- /hints ---

- Now the ball bounces until it reaches the far-left of the LED matrix. If this happens, the game should end, as the player hasn't managed to get the bat into place. Display a message to the player with the following code:

    ``` python
    if ball_position[0] == 0:
        sense.show_message("You Lose", text_colour=(255, 0, 0))
        quit()
    ```

- Run your code to watch the ball bounce and the game end.
