## Challenge: stuff


- Now the ball bounces until it reaches the far-left of the LED matrix. If this happens, the game should end, as the player hasn't managed to get the bat into place. Display a message to the player with the following code:

    ``` python
    if ball_position[0] == 0:
        sense.show_message("You Lose", text_colour=(255, 0, 0))
        quit()
    ```

- Run your code to watch the ball bounce and the game end.


- Can you change variable values to make the game easier or harder, by changing the `sleep` period?
- Can you add a score, which increases each time the ball bounces off the bat?
- How about giving the player three lives, and making them lose one each time they miss the ball?
