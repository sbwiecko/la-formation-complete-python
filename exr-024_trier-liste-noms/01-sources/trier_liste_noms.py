"""
On récupère les prénoms depuis le fichier .txt situé dans le dossier du script,
puis on nettoie cette liste avec la méthode strip(), e.g. espaces et doubles
espaces, virgules et points, saut de ligne etc., et en sauvegarde cette liste des
prénoms triés par ordre alphabétique dans un autre fichier avec un nom par ligne.
"""

import os

# dossier racine où se trouve le fichier à traiter
root = os.path.dirname(__file__)
filepath = os.path.join(root, "prenoms.txt")

# on récupère le contenu du fichier
with open(filepath, 'r', encoding="utf8") as file:
    str_names = file.read()

list_names = str_names.split(',') # all whitespaces are processed by default, i.e. space, \n and \t
list_names_cleaned = [_.strip(" \n;.") for _ in list_names if _ is not ' ']
print(list_names_cleaned)