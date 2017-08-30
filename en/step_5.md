## Make a bat

Let's draw the rest of the bat by illuminating the LEDs immediately above and below the one that's currently illuminated. To do this, we will make a **function**.

[[[generic-python-simple-functions]]]

+ **Indent** the line `sense.set_pixel(0, bat_y, white)` by putting your cursor at the start of the line and pressing the **tab** key.

+ On the line immediately above this line, start a function called `draw_bat`:

![Indented part of function](images/indented-in-function.png)

The lines following the start of a function are indented to show that they are **inside** the function.

+ Add two more lines of code **inside** the function to illuminate the LEDs at positions `bat_y + 1`, and `bat_y - 1` as well.

--- hints ---
--- hint ---
The lines you need are very similar to the one you already have. What do you need to change in this line to make `bat_y + 1` lit instead of `bat_y`?

```python
sense.set_pixel(0, bat_y, white)
```
--- /hint ---

--- hint ---
Here is how your function should look:

```python
def draw_bat():
	sense.set_pixel(0, bat_y, white)
	sense.set_pixel(0, bat_y + 1, white)
	sense.set_pixel(0, bat_y - 1, white)
```

--- /hint ---

--- /hints ---

If you run your code now, nothing will happen. The code you just wrote inside the function will not do anything at all until the function is **called**.

+ Add a line of code underneath the function and **not indented** to call the function.

```python
draw_bat()
```

+ Run the code and check that three LEDs are now illuminated

![Three LEDs](images/three-leds.png)
