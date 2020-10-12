## Verlicht een LED

Games gebruiken vaak de coördinaten `x` en `y` om te bepalen waar een object op het display staat. `x` wordt gebruikt om de horizontale positie van een object in te stellen en `y` wordt gebruikt om de verticale positie van een object in te stellen.

We kunnen hetzelfde doen met de LED's op de Sense HAT.

[[[rpi-sensehat-led-coordinates]]]

Laten we ons Pong-spel beginnen door een enkele LED op te lichten om een bal te maken en vervolgens een paar extra toe te voegen om een batje te maken.

+ Open IDLE als je een fysieke Sense HAT gebruikt, of open een nieuwe trinket als je de [emulator](http://trinket.io/sense-hat) gebruikt.

[[[rpi-gui-idle-opening]]]

+ Voeg deze code toe aan het begin van je bestand om de `sense_hat` module te importeren en verbinding te maken met de Sense HAT.

```python
from sense_hat import SenseHat
sense = SenseHat()
```

+ Het batje zal wit zijn. Definieer een variabele met de naam `wit` en stel de waarde in op `(255, 255, 255)`, wat de RGB-kleurrepresentatie van wit is.

[[[rpi-sensehat-display-colour]]]

[[[generic-theory-colours]]]

Het batje bevindt zich altijd in de meest linkse kolom met pixels, dus de waarde `x` is altijd `0`, maar de waarde `y` verandert als je het batje op en neer beweegt.

+ Maak nog een variabele `bat_y` en stel de waarde in op `4`.

+ Stel de LED op positie `(0, bat_y)` in op `wit` met de methode `set_pixel`.

[[[rpi-sensehat-single-pixel]]]

--- hints ---


--- hint ---

Maak eerst een variabele met de naam `wit` en stel deze als volgt in op `(255, 255, 255)`:

```python
wit = (255, 255, 255)
```

--- /hint ---

--- hint ---

Maak op de volgende regel een andere variabele net zoals je deed voor de kleur `wit`, behalve deze keer is de naam `bat_y` en de waarde `4`.

--- /hint ---

--- hint ---

Je voltooide code moet er zo uitzien:

```python
from sense_hat import SenseHat
sense = SenseHat()

wit = (255, 255, 255)

bat_y = 4

sense.set_pixel(0, bat_y, wit)
```

--- /hint---

--- /hints ---

+ Bewaar en voer je code uit. Een enkele LED moet nu wit aan de linkerkant van de LED-matrix worden verlicht.

![Enkele LED brandt](images/single-led.png)
