#####################################
#            Dependencies           #
#####################################

from Soldes import Salle
import copy

#####################################
#                Class              #
#####################################
class Magasin:
    #####################################
    #                Init               #
    #####################################
    def __init__(self):
        self.salles = [] # Les salles du magasin
        self.actualWay = [[0]] # Le chemin que l'on a fait
        self.tempWay = [0] # Le chemin qu'on est en train de faire
        self.result = [[],9999] # Le chemin le plus court
    # Ajout d'une salle dans le magasin
    def addSalle(self,pds):
        self.salles.append(Salle.Salle(self,pds))
        return len(self.salles)-1
    # Création d'une liaison entre deux salles
    def linkSalle(self,nA,nB):
        self.salles[int(nA)].addSalle(int(nB))
        self.salles[int(nB)].addSalle(int(nA))
    # Définie l'entrée et la sortie
    def setExit(self,n):
        self.salles[int(n)].setExit()
    def setEntry(self,n):
        self.salles[int(n)].setEntry()
    #####################################
    #               Debug               #
    #####################################
    # Affiche les propriétés de chaque salle
    def log(self):
        for i in self.salles:
            i.log()
    #####################################
    #                Main               #
    #####################################
    # Commence le calcul par l'entrée
    def start(self):
        self.salles[0].calc() # Demande à l'entrée de calculer les chemins qui partent d'elle
        # Affiche les propriétés du chemin le plus rapide
        print()
        print("Chemin w/ somme + faible : {}".format(str(self.result[0])))
        print("Somme du chemin : {}".format(str(self.result[1])))
        return
    # On demande à la salle suivante de calculer
    def nextSalle(self,nb):
        # Si on est arrivé à la sortie
        if nb == len(self.salles)-1:
            print("Chemin : {}, S = {}".format(str(self.tempWay),self.sommePoids())) # On l'affiche et on regarde si le chemin est plus court
            return # On revient à la salle précédente
        # Si le chemin auquel on tente d'aller fait pas parti du chemin emprunté
        if not(nb in self.tempWay):
            self.tempWay.append(nb) # On ajoute au chemin actuel
            self.actualWay.append(copy.deepcopy(self.tempWay)) # On ajoute le chemin actuel au chemin emprunté
            self.salles[nb].calc() # On calcule la suite du chemin
            return # Puis on retourne à la salle précédente
        else: # Sinon, le chemin est bloqué (on évite les boucles infinies) donc on revient en arrière
            return
    # Si le chemin est bloqué, on enlève la salle actuelle et on enlève le chemin actuel du log de l'évolution du chemin
    def blocked(self):
        if (len(self.actualWay) != 0): # Si le chemin n'est pas de longueur 0
            self.actualWay.pop()
            self.tempWay = copy.deepcopy(self.actualWay[-1])
        return # Puis on revient à la salle
    # On calcule le temps nécessaire pour prendre le chemin calculé et on compare par rapport au meilleur chemin enregistré
    def sommePoids(self):
        s = 0
        # Calcul du temps
        for i in self.tempWay:
            if (i != 0):
                s += (self.salles[i].getPds() + 50)/50
        # Comparaison
        if s < self.result[1]:
            self.result[0] = self.tempWay
            self.result[1] = s
        return s # On retourne le temps