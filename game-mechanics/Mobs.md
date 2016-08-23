## Mobs

les mobs arrivent par vague depuis les 4 entrées du stage (au centre des 4 côtés du stage).
Il existe différents types de mobs. Chaque type est décliné en 3 tailles (normal, alpha, boss).

Eliminer un mob rapporte de l'argent (montant variant en fonction du mob). L'argent permet au joueur d'acquérir de nouvelles tourelles, et donc de survivre aux prochaines vagues de Mobs.

Il existe deux grands types de Mobs :
Les mobs terrestres -> ils sont affectés par les obstacles et sont plus lents et plus robustes.
Les mobs aériens -> les obstacles ne les affectent pas. Ils sont plus rapides mais plus vulnérables.

## Design des mobs

# Couleur
Les mobs ont un comportement variable en fonction de la couleur :
- vert : IA classique. Suit le chemin le plus court jusqu'à la tourelle principale
- bleu : IA Prudente. Suite le chemin le plus sûr (le moins à portée des tourelles) jusqu'à la tourelle principale
- rouge : IA kamikaze. Explose sur la première tourelle qu'elle rencontre.
- violet : IA tactique. Suit le chemin le plus sûr jusqu'à la tourelle la plus vulnérable et explose dessus.

#Forme
mobs terrestres : forme plutot ronde (bulle ou boule roulante) qui campent au contact d'une tourelle.

diggers mobs :	certains mobs pourront sortir de terre au milieu du terrain au lieu de spawner sur le bord. Pour les différencier des mobs terrestres classiques, ils seront de couleur brune claire (IA verte) et brune foncée (IA rouge)

mobs volants : les mobs volants sont en forme de triangle.
