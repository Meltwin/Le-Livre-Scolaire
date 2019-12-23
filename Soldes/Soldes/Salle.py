class Salle:
    #####################################
    #                Init               #
    #####################################
    # Initialisation des salles avec leur magasin {mag} et leur poids (la promotion dans la salle) {pds}
    def __init__(self,mag,pds):
        self.mag = mag
        self.pds = pds
        self.salles = [] # On prépare les liaisons
        # Var pour savoir si exit ou entry
        self.exit = False 
        self.entry = False
    # Ajout d'une liason à une autre salle de numéro n (indice numéro dans tableau du magasin)
    def addSalle(self,n):
        self.salles.append(n)
    # Si entrée ou sortie
    def setExit(self):
        self.exit = True
    def setEntry(self):
        self.entry = True
    #####################################
    #                Debug              #
    #####################################
    # Affiche les propriétés de la salle
    def log(self):
        print(str(self.pds)+"% : "+str(self.salles))
    #####################################
    #                Calc               #
    #####################################
    # Parcours l'ensemble de ses laisons pour continuer le chemin    
    def calc(self):
        for i in self.salles:
            self.mag.nextSalle(i)
        # Si la salle n'est pas l'entrée
        if (not(self.entry)):
            # On dit que le chemin est bloqué (on revient dans une case où on est dékà passé) : on évite de tourner en rond
            self.mag.blocked()
        return # On en a fini avec cette salle, on revient en arrière
    # Retourne la promotion de la salle
    def getPds(self):
        return self.pds