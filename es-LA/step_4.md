## Enciende un LED

Por lo general, los juegos usan las coordenadas `x` y `y` para determinar dónde se ubica un objeto en el monitor. `x` se utiliza para posicionar un objeto de forma horizontal, y `y` para posicionar un objeto de forma vertical.

Lo mismo podemos hacer con los LEDs en la Sense HAT.

[[[rpi-sensehat-led-coordinates]]]

Comencemos el juego encendiendo un LED para crear una pelota y agregar algunas más para crear un bate.

+ Open IDLE if you are using a physical Sense HAT, or open a new trinket if you are using the [emulator](http://trinket.io/sense-hat).

[[[rpi-gui-idle-opening]]]

+ Add this code at the start of your file to import the `sense_hat` module and connect to the Sense HAT.

```python
from sense_hat import SenseHat
sense = SenseHat()
```

+ El bate será blanco. Define a variable called `white`, and set its value to `(255, 255, 255)`, which is the RGB colour representation of white.

[[[rpi-sensehat-display-colour]]]

[[[generic-theory-colours]]]

El bate siempre estará a la izquierda de los píxeles, así que el valor de `x` siempre será `0`, pero su valor `y` cambiará al mover el bate hacia arriba y hacia abajo.

+ Crea otra variable `bate_y` y asígnale el valor `4`.

+ Set the LED at the position `(0, bat_y)` to `white` using the `set_pixel` method.

[[[rpi-sensehat-single-pixel]]]

--- hints ---

--- hint ---

Primero, crea una variable con el nombre `blanco` y ajústala para que sea igual a `(255, 255, 255)` de esta manera:

```python
blanco = (255, 255, 255)
```

--- /hint ---

--- hint ---

En la siguiente línea, crea otra variable como hiciste para el color `blanco`, excepto que esta vez, el nombre será `bate_y` y el valor será `4`.

--- /hint ---

--- hint ---

Your finished code should look like this:

```python
from sense_hat import SenseHat
sense = SenseHat()

blanco= (255, 255, 255)

bate_y = 4

sense.set_pixel(0, bate_y, blanco)
```

--- /hint---

--- /hints ---

+ Guarda y ejecuta tu código. Ahora debería encenderse un solo LED en blanco en el lado izquierdo de la matriz de LED.

![Un solo LED encendido](images/single-led.png)
