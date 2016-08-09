# Création d'un jeu en vue isométrique

## Principe de l'approche "tile-based"

Dans l'approche "tile-based", chaque élément visuel (personnage, décor, bâtiments...) est décomposé en briques élémentaires d'une taille fixée : les cases (_tiles_). On modélise ces cases sur une matrice 2D et on les utilise pour construire la représentation isométrique.

Chaque case peut être d'un type spécifique, comme on l'a déjà fait dans le tank game : herbe, mur, roche, sable ... On les encode par des numéros dans la matrice des cases.

Par ex on représente des murs par 1 et de l'herbe par 0 et on peut construire une map avec une matrice du type :

```
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
```

Concrètement dans Pygame, on va avoir à notre disposition une palette de cases (une sorte de bibliothèque à surfaces pré-chargées) que l'on va blitter sur la surface de l'écran.

La taille de chaque case étant choisie (ex: 50px*50px), le plus simple sera d'utiliser des images de base de la même taille (comme on l'a toujours fait).

## Projection isométrique

### Le principe

Il s'agit effectivement d'une **projection** : on passe d'une vue top-down (2D classique, cartésienne) à une vue isométrique. Pour cela, **la caméra pivote de 45°à gauche ou à droite** (les diagonales de la map forment un + au lieu d'un x) **puis de 30°vers le bas**. Ces angles sont choisis pour que les cases forment des **losanges 2x plus larges qu'ils ne sont hauts**.

> Conséquence importante : un `Rect(top, left, width, height)` a une largeur et hauteur isométrique de `(width, height/2)`. Donc les cases ont une taille cartésienne `(TILE_SIZE, TILE_SIZE)` et une taille isométrique `(TILE_SIZE, TILE_SIZE/2)`.

Ces angles étant donnés, on peut déterminer une relation directe entre les coordonnées cartésiennes `(x, y)` d'une case et ses coordonnées isométriques `(xi, yi)` (ces coordonnées étant en effet les coordonnées "à l'écran") :

```python
# Transformation des coordonnées d'une case
# cartésien -> isométrique
xi = x - y
yi = (x + y) / 2

# isométrique -> cartésien
x = (2*yi + xi) / 2
y = (2*yi - xi) / 2
```

On voit donc bien que ** $x$ peut varier de `- TILE_SIZE` à `+ TILE_SIZE`**, et qu'en revanche **$y$ varie entre `0` et `+ TILE_SIZE`**.

Par exemple, prenons une map carrée de 100 cases de côté et calculons les coordonnées isométriques de chaque coin :


| `(x, y)` | `(xi, yi)` |
|:----------:|:----------:|
|`(0, 0)`| `(0, 0)`|
|`(100, 0)`|`(100, 50)`|
|`(0, 100)`|`(-100, -50)`|
|`(100, 100)`|`(0, 100)`|

### Premiers tests

Voir `test_results_img/basic_isometric_rendering.png`. 