"""
On récupère les prénoms depuis le fichier .txt situé dans le dossier du script,
en considérant que les séparations sont soit une virgule soit un saut de ligne,
puis on nettoie cette liste avec la méthode strip(), e.g. espaces et doubles
espaces, virgules et points, saut de ligne etc., et en sauvegarde cette liste des
prénoms triés par ordre alphabétique dans un autre fichier avec un nom par ligne.
"""

import os

# dossier racine où se trouve le fichier à traiter
root = os.path.dirname(__file__)
filepath = os.path.join(root, "prenoms.txt")

# on récupère le contenu du fichier
with open(filepath, 'r', encoding="utf8") as file: # utf-8 car soucis avec les accents
    str_names = file.read()

# j'ai opté pour un remplacement des '\n' en ', ' pour un split global
# mais on pourrait utiliser les expressions régulières
str_names = str_names.replace('\n', ', ').replace('.', ',').replace(' ',',')
# remplace aussi les points et espaces mais là c'est vraiment une BD pourrie

list_names = str_names.split(',')
# on rajoute un \n à chaque item pour permettre le writelines
list_names_cleaned = [_.strip()+'\n' for _ in list_names if _]
list_names_ordered = sorted(list_names_cleaned)

# et on sauvegarde le tout dans un nouveau fichier
with open("liste_prenoms_tries.txt", 'w', encoding="utf8") as f:
    f.writelines(list_names_ordered)