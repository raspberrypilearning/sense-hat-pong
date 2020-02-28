## Collision with the bat

Now that the ball bounces in both directions, let's make it bounce off the bat.

The bat is always situated in the far left column of the LED grid, so its `x` coordinate is always `0`.

The ball will bounce off the bat if it is in the row next to the bat — that is, if the ball's `x` position is equal to `1`.

![Ball bounce x](images/ball-bounce-x.png)

+ Add this code to the end of the `draw_ball` function:

``` python
if ball_position[0] == 1:
    ball_velocity[0] = -ball_velocity[0]
```

This code will cause the ball to reverse direction if it reaches an `x` coordinate of `1`. But now the ball reverses regardless of whether the bat is there or not!

- Add to the condition to require the ball's `y` position to also (**and**) be anywhere between the top and bottom of the bat.

Remember that the bat is made up of three pixels. So for the ball to 'bounce off' the bat, the `y` coordinate of the ball can be anywhere **between** the top of the bat (`bat_y - 1`) and the bottom of the bat (`bat_y + 1`).

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

This condition checks whether `x` is between `1` and `10` (inclusive) by asking first whether `1` is less than or equal to `x`, and then whether `x` is less than or equal to `10`. Use a similar line of code to determine whether your ball's `y` coordinate is between `bat_y - 1` and `bat_y + 1`.

--- /hint ---
--- hint ---

Here is how your finished code should look. The bit you should add is highlighted in blue:

![Has it hit the bat?](images/hint-add-hit-bat-solution.png)

--- /hint ---

--- /hints ---

+ Save and run your code. Check that the ball bounces off the bat only when the bat is in the correct position!
