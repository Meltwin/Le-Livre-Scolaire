##########################################
#                Functions               #
##########################################
# Table de correspondance entre le numéro de la combinaison et sa forme
def returnForme(x):
    if (x == 0):
        return "abcd"
    elif (x == 1):
        return 'abc + d'
    elif (x == 2):
        return "ab + cd"
    elif (x == 3):
        return 'a + bcd'
    elif (x == 4):
        return "ab + c + d"
    elif (x == 5):
        return "a + bc + d"
    elif (x == 6):
        return "a + b + c + d"

##########################################
#                   Main                 #
##########################################
compte = [[0]*7 for i in range(7)] # Tableau de 7x7 pour chaque combinaison en ligne et en colonne
t = [0]*7 # Tableau pour chaque valeur de chaque combinaison

# Pour chaque chiffre strictement différent des autres
for a in range(10):
    for b in range(10):
        if (b != a):
            for c in range(10):
                if (c != b and c !=a):
                    for d in range(10):
                        if (d!=a and d!=b and d!=c):
                            # On calcule les combinaison
                            t[0] = a*1000 + b*100 + c*10 + d
                            t[1] = a*100 + b*10 + c + d
                            t[2] = a*10 + b + c*10 +d
                            t[3] = a+ b*100 + c*10 + d
                            t[4] = a*10 + b + c + d
                            t[5] = a + b*10 + c +d
                            t[6] = a +b +c +d

                            # On test les égalités des combinaisons
                            for i in range(7):
                                for j in range(7):
                                    if (j != i):
                                        if (t[i] == t[j]):
                                            compte[i][j] +=1
                                            print("m = {0},a = {1}, r= {2}, s= {3} {4} <-> {5} [{6}]".format(a,b,c,d,returnForme(i),returnForme(j),t[i]))
print()
##########################################
#                 Result                 #
#                 display                #
##########################################
for i in range(7):
    for j in range(7):
        print("{0} <-> {1} = {2}".format(returnForme(i),returnForme(j),compte[i][j])) # Affiche le couple de combinaison