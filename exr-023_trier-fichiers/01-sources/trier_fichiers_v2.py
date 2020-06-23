import os
import shutil # high-level operations on files and collections of files (copying and removal)
from glob import glob

# d'abord on récupère le chemin de la racine du fichier .py courant
racine = os.path.dirname(__file__)

# maintenant in recherche chaque fichier avec une 'extension' précise dans le 'dossier_recherche'
# et on le met dans le dossier correspondant grace à un dictionnaire
dossier_recherche = os.path.join(racine, "tri_fichiers_sources")

extensions_dic = {
    'Documents': ['pdf'],
    'Images':    ['jpg', 'jpeg', 'png'],
    'Musique':   ['mp3', 'wav'],
    'Videos':    ['mp4', 'mov'],
}

for dossier_destin, extensions in extensions_dic.items():        # pour chaque dossier destination sa liste d'extensions
    chemin_dossier_dest = (os.path.join(racine, dossier_destin)) # ce chemin sera utilisé ici et plus loin
    os.makedirs(chemin_dossier_dest, exist_ok=True)              # dossier à créer s'il n'existe pas encore

    for extension in extensions:                                 # et pour liste chaque extension de la liste
        # on liste les fichiers avec cette extension et appartenant au dossier de recherche
        for file in glob(os.path.join(dossier_recherche, "*." + extension), recursive=True): # on sait jamais pour recursive
            # on copie vers le dossier de destination
            shutil.copy(file, chemin_dossier_dest)
            # on copie pour garder le dossier test intact mais ou pourrait utiliser shutil.move dans un script réel