## Lighting up an LED

Let's start our Pong game by lighting up a single LED, and then a few more to create a bat.

- Click on `Menu` > `Programming` > `Python 3 (IDLE)`. Then, in the window that opens up, click on `File` and `New File`. The second window that opens is where you will write your code.

- First, you'll need to import the `sense_hat` and `time` modules. Type the following into your file:

	```python
	from sense_hat import SenseHat
    from time import sleep
    
	sense = SenseHat()
	```

- If you are using the emulator as opposed to the physical Sense HAT, you need to change one line, so that the above code reads:

    ``` python
    from sense_emu import SenseHat
    from time import sleep

    sense = SenseHat()
    ```

- The bat will always be on the far-left column of pixels, so its `x` value will always be `0`, but the `y` value will change as you move the bat up and down. Start by setting the `y` value to 4, by adding this line:

	```python
	y = 4
	```

- You can now illuminate your first LED using the following line of Python:

	```python
	sense.set_pixel(0, y, 255, 255, 255)
	```

- The values `(0, y, 255, 255, 255)` indicate the `x` and `y` position of the LED, and the colour of light it should emit. `255, 255, 255` is white.

- Save your file by holding down the `Ctrl` key and then pressing the `S` key. Call it  `pong.py`, then run it by pressing `F5`.

	A single LED should now be illuminated. 

![Single LED](images/1-led.png)

