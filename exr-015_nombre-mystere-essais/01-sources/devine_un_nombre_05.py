"""
1. Ajouter une boucle pour permettre à l'utilisateur jusqu'à 5 essais pour trouver le nombre mystère.
2. Si l'utilisateur trouve le nombre mystère avant les 5 essais, indiquer qu'il a gagné.
3. Si l'utilisateur ne trouve pas le nombre mystère au bout des 5 essais, indiquer qu'il a perdu et afficher le nombre mystère.
"""

import random

nombre_mystere = random.randint(0, 10)
nombre_essais = 1

while nombre_essais < 6:
    nombre = input("Quel est le nombre mystère ? ")
    if not nombre.isdigit():
        print("SVP, entrez un nombre valide.")
        continue
    
    nombre = int(nombre)

    if nombre > nombre_mystere:
        print(f"Le nombre mystère est plus petit que {nombre}")
    elif nombre < nombre_mystere:
        print(f"Le nombre mystère est plus grand que {nombre}")
    else:
        print("Bravo, vous avez trouvé le nombre mystère !")
        exit()
    
    nombre_essais += 1

print(f"Perdu... Le nombre mystère était {nombre_mystere}")