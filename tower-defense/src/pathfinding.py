# ------ Implementation de l'algorithme de Dijsktra ------

class FilePrio:
    ''' une file de priorité implémentée en tas'''

    def __init__(self,length):
        self.data = [None]*length
        self.len = 0
        self.lenmax = length

    def vide(self):
        ''' True si la file est vide
            False sinon'''
        return (self.len == 0)

    def plein(self):
        ''' True si la file est pleine
            False sinon '''
        return (self.len == self.lenmax)

    def __len__(self):
        return self.len

    def permute(self,i,j):
        self.data[i],self.data[j] = self.data[j], self.data[i]

    def monte(self,k):
        if k>0 :
            i = (k-1)//2
            if self.data[i].key > self.data[k].key :
                self.permute(k,i)
                self.monte(i)

    def descend(self,k):
        if 2*k+1 < self.len :
            if 2*k+2 == self.len or self.data[2*k+1].key < self.data[2*k+2].key :
                i = 2*k+1
            else :
                i = 2*k+2
            # i est l'indice du fils de k avec la plus petite clé
            if self.data[k].key > self.data[i].key :
                self.permute(k,i)
                descend(self,i)

    def append(self,x,p):
        if self.plein():
            raise UserWarning("La file de priorité est pleine")
        self.data[self.len] = Event(x,p)
        self.monte(self.len)
        self.len +=1
        
    def pop(self):
        if self.vide():
            raise UserWarning("La file de priorité est vide")
        output = self.data[0]
        self.len -=1
        self.data[0] = self.data[self.len]
        self.descend(0)
        return output
                
def study_voisins(x,y,dist,dejavu,file,passage) :
    (jx,ix) = x
    (jy,iy) = y
    ndist = dist[ix][jx]+1
    if (not dejavu[iy][jy]) and ndist < dist[iy][jy] :
        file.append(y,ndist)
        dist[iy][jy] = ndist
        passage[iy][jy] = (jx,ix)
    return dist,file,passage
    
def study_voisins_list(x,list,dist,dejavu,file,passage) :
    for y in list :
        dist,file,passage = study_voisins(x,y,dist,dejavu,file,passage)
    return dist,file,passage

def get_voisins(matrice,i,j) :
    voisins = []
    if i>0 : 
        if matrice[i-1][j] : voisins.append((j,i-1))
    if i<60 :
        if matrice[i+1][j]  : voisins.append((j,i+1))
    if j>0 :
        if matrice[i][j-1] : voisins.append((j-1,i))
    if j<60 :
        if matrice[i][j+1] : voisins.append((j+1,i))
    return voisins

def clean(list) : #enlève les points inutiles d'une liste de (x,y)
    new_list = [x for x in list]
    poped = 0
    for i in range(1,len(list)-1) :
        (xi,yi) = list[i]
        (xsuiv,ysuiv) = list[i+1]
        (xprec,yprec) = list[i-1]
        if (xi==xsuiv and xi==xprec) or (yi==ysuiv and yi==yprec) : #on enlève le point du milieu si 3 points sont alignés
            new_list.pop(i-poped)
            poped+=1
    return new_list 

def get_new_path(depart,arrivee,obstacles) : #algorithme de Dijsktra 
        (jd,id) = depart
        (ja,ia) = arrivee           

        dejavu = [[False for i in range(32)] for j in range(21)] #les points déjà visités par l'algorithme
        
        distance= [[100000 for i in range(32)] for j in range(21)]  #la matrice des distances: : distance[i][j] est la distance minimale 
                                                                                                 #trouvée pour l'instant pour aller de la case de départ à la case (i,j)
                                                                                                 # initialisée avec une valeur représentant une distance infinie
        distance[id][jd] = 0
        
        
        passage = [[(-1,-1) for i in range(32)] for j in range(21)] #passage[i][j] contient le voisin de (j,i) qui est sur le plus court chemin allant du départ à (j,i)
        chemin_case = []
        
        file_prio = FilePrio(3600) #file de priorité gérant les arêtes.
        file_prio.append((jd,id),0)

        while not dejavu[ic][jc] : #tant que l'on a pas atteint la case de la cible
            x = file_prio.pop()
            (jx,ix) = x
            if not dejavu[ix][jx] :
                list = get_voisins(obstacles,ix,jx)
                distance,file_prio,passage = study_voisins_list(x,list,distance,dejavu,file_prio,passage)
                dejavu[ix][jx] = True
        
        while (ja,ia) != (jd,id) : #tant que la position n'est pas au départ, le chemin n'est pas complété
            chemin_case.append((jc,ic))
            (jc,ic) = passage[ic][jc]

        chemin_case = clean(chemin_case)
        chemin_case.reverse() #on prend le chemin allant du départ à l'arrivée (liste dans le sens inverse par construction)

        chemin = []
        for x in chemin_case :
            (jx,ix) = x
            chemin.append((10*jx+5,10*ix+5))
        return chemin