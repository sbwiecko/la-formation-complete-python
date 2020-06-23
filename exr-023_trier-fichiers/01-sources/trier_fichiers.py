"""
mp3, wav : Musique
mp4, mov : Videos
jpg, jpeg, png : Images
pdf : Documents
"""

import os
import shutil # high-level operations on files and collections of files (copying and removal)
import glob

# d'abord on créée les dossiers s'ils n'existent pas, à la racine du fichier .py courant
racine = os.path.dirname(__file__)
dossiers = ['Musique', 'Videos', 'Images', 'Documents']

for dossier in dossiers:
    path_dossier = os.path.join(racine, dossier)
    if not os.path.exists(path_dossier):
        os.mkdir(path_dossier)

# maintenant in recherche chaque fichier avec une 'extension' précise dans le 'dossier_recherche'
# et on le met dans le dossier correspondant grace à un dictionnaire
dossier_recherche = os.path.join(racine, "tri_fichiers_sources")

extensions_dic = {
    'Documents': ['pdf'],
    'Images':    ['jpg', 'jpeg', 'png'],
    'Musique':   ['mp3', 'wav'],
    'Videos':    ['mp4', 'mov'],
}

for dossier_destin, extensions in extensions_dic.items(): # pour chaque dossier destination sa liste d'extensions
    for extension in extensions:                          # et chaque extension de la liste
        
        # on liste les fichiers avec cette extension et appartenant au dossier de recherche
        for file in glob.glob(os.path.join(dossier_recherche, "*." + extension), recursive=True): # on sait jamais pour recursive
            
            # on copie pour garder le dossier test intact mais ou pourrait utiliser shutil.move dans un script réel
            shutil.copy(file, os.path.join(racine, dossier_destin))