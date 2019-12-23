##########################################
#              Dependencies              #
##########################################
import copy

##########################################
#                Functions               #
##########################################
# Fonction qui permet de savoir si toute la salle est contaminée
def isAllZombie():
    global salle
    global n
    global m

    etat = True

    for i in range(n):
        for j in range(m):
            if (salle[i][j] == 0): # Si non contaminé
                etat = False
    return etat
def printSalle():
    global salle
    for i in range(n):
        print(salle[i])
    print()
    input()

##########################################
#                   Main                 #
##########################################
# Init
#   On récupère la taille de la salle
n = int(input("Largeur : "))
m = int(input("Longueur : "))

salle = [[0] * m for _ in range(n)] # On créé la salle
salle[int((n-1)/2)][int((m-1)/2)] = 1 # On place le zombie au centre
minutes = 0 # Temps initial = 0

while (not(isAllZombie())): # Tant que tout le monde n'est pas infecté
    salleTemporaire = copy.deepcopy(salle) # On créé une copie de la salle que l'on va modifier
    minutes = minutes + 1 # On incrémente le temps 
    #printSalle() # Facultatif : pour voir l'état de la contamination
    for i in range(0,n):
        for j in range(0,m):
                if (salle[i][j] == 1): # Si contaminé, on contamine tout autour
                    if (j != 0): 
                        salleTemporaire[i][j-1] = 1
                    if (j != m-1):
                        salleTemporaire[i][j+1] = 1
                    if (i != 0):
                        salleTemporaire[i-1][j] = 1
                    if (i != n-1):
                        salleTemporaire[i+1][j] = 1
    salle = salleTemporaire # On remplace l'ancienne par la nouvelle

##########################################
#                 Result                 #
#                 display                #
##########################################
print("Minutes nécessaires = "+str(minutes)) # Temps
print((n/2)+(m/2)-1) # Corrélation avec la formule