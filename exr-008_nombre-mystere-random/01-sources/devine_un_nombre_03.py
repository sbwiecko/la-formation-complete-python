# Remplacer le nombre mystère par un nombre aléatoire
import random
nombre_mystere = random.randrange(10)

nombre_utilisateur = input("Quel est le nombre mystère ? ")

resultat = int(nombre_utilisateur) == nombre_mystere
print(resultat)