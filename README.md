# MC Tower Defense
_A cool Python game about defending a tower.  
All your base are belong to us._


## Principes de base du Tower Defense.

Le joueur contrôle une **base**.

L'objectif du jeu est de **défendre cette base contre les invasions ennemies**.

Le jeu sera rendu en **3D isométrique**. La base sera au centre. Il y aura 4 points d'apparition d'ennemis, un à chaque coins de la map a priori.

La base a une barre de vie. Chaque coup d'un ennemi entame cette barre de vie. Une fois réduite à zéro, la partie est a priori finie.

Le joueur peut implanter des "tourelles" qui obstrueront le passage de l'ennemi vers la base. C'est là l'élément principal de la stratégie du joueur.


## Idées à développer

Le terme "tourelle" est peut-être à revoir, puisqu'elles pourront vraisemblablement être de différents types : offensif, défensif, soins intensifs... On peut imaginer

Il devra exister une monnaie d'échange pour implanter ou upgrader les tourelles. Ça peut être fonction des ennemis tués, du temps écoulé, etc. Les tourelles pourront peut-être aussi être réparées (au lieu d'être anéanties et de disparaître immédiatement --> compte à rebours pour la réparation ?).

Les vagues d'ennemis devront avoir une sorte d'identité, _i.e._ un nombre d'ennemi fixé et uniquement certains types d'ennemis. Ça pourra servir par exemple à introduire de nouveaux types d'ennemis au fur et à mesure.

On peut développer le jeu autour d'un cycle :

- introduction d'un nouvel ennemi dans une vague qui le met en valeur
- une ou plusieurs nouvelles vagues qui combinent cet ennemi à d'autres types déjà vus précédemment
- un super-ennemi qui descend du nouveau type d'ennemi, qui peut faire office de "boss".