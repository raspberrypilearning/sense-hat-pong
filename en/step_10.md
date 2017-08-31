## You lose

If you miss the ball with the bat, at the moment it bounces off the far left wall. Let's change the code so that if the player misses the ball, they lose the game.

+ Add another `if` statement at the end of your `draw_ball` function to check whether the ball's `x` position equals `0` - the far end of the screen.

+ If this condition is true, display the message "You lose".

--- hints ---
--- hint ---
Add your new `if` statement here. It will look very similar to the conditions you have already written.

![You lose](images/lose-hint-add-code.png)
--- /hint ---

--- hint ---
Here is how your code should look. The part to add is highlighted in blue:

![You lose](images/you-lose-hint-solution.png)
--- /hint ---
--- /hints ---

+ Save and run your code. Check that if you miss the ball, the message "You lose" appears. The game will restart after the message has been displayed.
