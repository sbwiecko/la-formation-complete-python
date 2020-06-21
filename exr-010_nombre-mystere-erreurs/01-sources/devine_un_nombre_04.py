"""
1. Rajouter une structure conditionnelle pour vérifier si l'élément entré par l'utilisateur est bien égal à un nombre.
2. Si c'est le cas, continuer avec la structure conditionnelle qui vérifie si le nombre est plus petit, plus grand ou égal au nombre entré.
3. Sinon, affichez un message d'avertissement à l'utilisateur pour lui demander d'entrer un nombre.
"""

import random

nombre_mystere = random.randint(0, 10)
nombre = input("Quel est le nombre mystère ? ")
if nombre.isdigit():
    nombre = int(nombre)

    if nombre > nombre_mystere:
        print(f"Le nombre mystère est plus petit que {nombre}")
    elif nombre < nombre_mystere:
        print(f"Le nombre mystère est plus grand que {nombre}")
    else:
        print("Bravo, vous avez trouvé le nombre mystère !")

else: print("Saisir un nombre...")