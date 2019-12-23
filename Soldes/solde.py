from Soldes import Magasin as mp

#####################################
#              Création             #
#             du magasin            #
#####################################

m = mp.Magasin() # On créé le magasin

#####################################
#              Création             #
#             des salles            #
#####################################

# On créé l'entrée
m.addSalle(0)
m.setEntry(0)

# On créé les autres salles
a = m.addSalle(40)
b = m.addSalle(9)
c = m.addSalle(8)
d = m.addSalle(10)
e = m.addSalle(30)
f = m.addSalle(50)
g = m.addSalle(5)
h = m.addSalle(30)
j = m.addSalle(25)
# On créé la sortie
i = m.addSalle(0)
m.setExit(i)

#####################################
#              Création             #
#            des liaisons           #
#####################################

m.linkSalle(a,0)
m.linkSalle(a,d)
m.linkSalle(a,b)
m.linkSalle(a,e)
m.linkSalle(b,c)
m.linkSalle(b,d)
m.linkSalle(c,d)
m.linkSalle(c,h)
m.linkSalle(d,g)
m.linkSalle(e,0)
m.linkSalle(e,f)
m.linkSalle(g,h)
m.linkSalle(h,i)
m.linkSalle(j,f)
m.linkSalle(j,i)

#####################################
#               Calcul              #
#####################################

# m.log() # Facultatif : affiche les salles, leur promotion et leur laisons avec les autres salles
m.start() # Lance le calcul