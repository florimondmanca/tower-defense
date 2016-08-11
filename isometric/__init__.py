'''
[17:51:45] Florimond Manca: « isoSprite » basique dont dériverait tout (mobs, tiles, décor, etc) serait pratique.
Parce qu’on va vite quand même se retrouver avec le pb du depth sorting
[17:53:42] Florimond Manca: donc si on implémente des trucs dans une classe de base isoSprite
(par ex, des attributs isoX, isoY, isoZ, isoDepth, la conversion entre les coordonnées iso et les coordonnées
cartésiennes/de map (que j’ai pour l’instant mis dans le module utils))
[17:54:08] Florimond Manca: ça sera peut-être plus pratique vu que tous les sprites qu’on créera à partir de ça
fonctionneront tous de la même manière, et une fois le pb de rendering réglé on devra plus s’en soucier
'''


class IsoSprite:

    def __init__(self):

        self.isoX = None
        self.isoY = None
        self.isoZ = None
        self.isoDepth = None
        

