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

### Bibliothèque de cases (TilePatch, TileLibrary)

Comme dit précédemment, on va utiliser des cases pré-fabriquées qu'on aura qu'à blitter à l'écran pour l'affichage : ce sont les `TilePatch`.
Un `TilePatch` associe simplement une image et un rect à une catégorie de case ("terrain", "building", etc.) et à un nom de case ("grass", "wallRock", "roadCornerNW", etc.).

Le dossier d'images de cases est situé `static/img/tiles`. Chaque catégorie de cases est un sous-dossier du dossier `tiles`.

Le fichier `tileslibrary` construit automatiquement tous les TilePatches à partir du contenu du dossier `tiles`.

Chaque catégorie a alors son propre dictionnaire qui est un attribut de l'objet `tlib`. Par exemple, pour obtenir le `TilePatch` de la case "grass" (qui est de la catégorie "terrain"), on utilise : `tlib.terrain_tiles["grass"]`. Et pour utiliser le `tlib` dans un module, on écrit `from .tileslibrary import tlib`. Je trouve ça assez simple d'utilisation et le fait que tout soit lié à la structure du dossier `tiles` permet de s'y retrouver assez facilement (même si c'était assez compliqué à coder ^^).

### Système de maps

Pour pouvoir tester l'isométrique, j'ai implémenté un mini-système de maps.

Un fichier de map est un fichier d'extension `.map`. Chaque fichier `.map` doit être construit de la même manière :

```python
WIDTH
"""donner la largeur de la map (nombre entier)"""
# exemple :
5
HEIGHT
"""donner la largeur de la map (nombre entier)"""
# exemple :
3

TILE_TYPES
"""indiquer les types de cases utilisées comme suit :
<symbole> <catégorie> <tile_type>"""
# exemple :
0 terrain grass
1 terrain roadNorth
END  # terminer par END

TILES_ARRAY
"""indiquer la map sous forme matricielle en utilisant
les symboles"""
# exemple :
00000
11111
00000
END  # terminer par END

END_OF_FILE  # termine le fichier
```

Actuellement, sur la `TILES_ARRAY`,  le nord pointe vers la gauche, le sud vers la droite, le 