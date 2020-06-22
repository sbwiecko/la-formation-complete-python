import os
import json
 
dossier_courant = os.path.dirname(__file__)
chemin_liste = os.path.join(dossier_courant, "liste.json")
 
if os.path.exists(chemin_liste):
    with open(chemin_liste, "r") as f:
        liste_de_courses = json.load(f)
else:
    liste_de_courses = []
 
affichage = """
Choisissez une option:
\t1: Ajouter un élément
\t2: Enlever un élément
\t3: Afficher la liste
\t4: Vider la liste
\t5: Terminer
"""
 
option = "0"
 
while option != "5":
    option = input(affichage)
    print(liste_de_courses)

# Comment rajouter deux options à l'intérieur de la boucle afin de permettre 
# à l'utilisateur d'ajouter ou d'enlever des éléments de la liste de courses ?

    if option == '1': liste_de_courses.append(input("Quel élément ajouter ? "))
    elif option == '2':
        if (item := input("Quel élément retirer ? ")) in liste_de_courses:
            liste_de_courses.remove(item)
