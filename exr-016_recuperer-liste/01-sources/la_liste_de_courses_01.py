"""
Comment récupérer la liste de courses depuis le fichier JSON si celui-ci existe ?
"""

import os
import json

# pour récupérer le chemin du dossier du fichier .py courant
dossier_courant = os.path.dirname(__file__)

# concaténer la variable 'dossier_courant' avec la chaîne de caractères 'liste.json'
path = os.path.join(dossier_courant, "liste.json")
print(path)
# si le fichier existe récupérer son contenu
if os.path.exists(path):
    with open(path, 'r') as file:
        liste_courses = json.load(file)

# sinon récupéere une liste vide
else : liste_courses = []