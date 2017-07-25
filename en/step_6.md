## Making a bat

- Next, we want to draw the rest of the bat by illuminating the LEDs immediately above and below the one that's currently illuminated. To do this, we're going to make a function. Delete the `sense.set_pixel(0, y, 255, 255, 255)` line, and then type the following:

	```python
	def draw_bat():
	```

- Now add three lines to your function to illuminate the LED at position `y`, `y + 1`, and `y - 1`:

	```python
	def draw_bat():
		sense.set_pixel(0, y, 255, 255, 255)
		sense.set_pixel(0, y + 1,255, 255, 255)
		sense.set_pixel(0, y - 1,255, 255, 255)
	```

- You can test your function works by **calling** it in the shell, which is the other IDLE window that should be open. Enter the following command:

	```python
	draw_bat()
	```

	When you press `Enter`, the LEDs should be illuminated.

	![Three LEDs](images/3-led.png)

	Your entire file should so far look like this:

		```python
		from sense_hat import SenseHat
		sense = SenseHat()

		y = 4

		def draw_bat():
			sense.set_pixel(0,y,255,255,255)
			sense.set_pixel(0,y+1,255,255,255)
			sense.set_pixel(0,y-1,255,255,255)
		```

