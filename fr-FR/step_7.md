## Créer une balle

L'étape suivante consiste à créer la balle. Mais avant, un peu de maths !

Une balle se déplaçant en deux dimensions a deux propriétés essentielles que tu dois considérer :

**Position** - comme la raquette, la balle a une coordonnée verticale et horizontale sur la grille.

**Vitesse** - la vitesse de la balle en ligne droite. Cela peut également être décrit par deux nombres : la vitesse à laquelle elle se déplace dans la dimension `x` et la vitesse à laquelle elle se déplace dans la dimension `y`.

+ Localise la variable `raquette_y` dans ton programme et, au-dessous, ajoute deux listes pour décrire les propriétés de la balle :

``` python
balle_position = [3, 3]
balle_vitesse = [1, 1]
```

+ Choisis une couleur pour ta balle et, sous ta variable `blanc`, définis une variable avec la valeur de la couleur choisie. Nous avons utilisé  `(0, 0, 255)`, ce qui correspond au bleu.

+ Dans la section des fonctions, crée une fonction appelée `dessine_balle`:

``` python
def dessine_balle():
```

+ Ajoute une ligne de code à la fonction `dessine_balle` pour allumer une LED à la `balle_position`.

[[[generic-python-list-index]]]

--- hints ---
--- hint ---

La position sur l'axe `x` sera l'élément zéro de la liste `balle_position`. La position `y` sera le premier élément de la liste `balle_position`.

--- /hint ---

--- hint ---

Voici à quoi devrait ressembler ton code (en supposant que tu aies également choisi la couleur bleue pour ta balle) :
``` python
def dessine_balle():
    sense.set_pixel(balle_position[0], balle_position[1], bleu)
```

--- /hint ---
--- /hints ---

+ Dans ta boucle `while`, appelle la fonction `dessine_balle`.

+ Enregistre et exécute ton code et vérifie que la balle est affichée sur la matrice LED.

![Dessine la balle](images/draw-ball.png)
