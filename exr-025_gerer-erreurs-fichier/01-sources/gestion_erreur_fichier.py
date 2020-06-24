"""
1. Gérer l'erreur qui arrive quand l'utilisateur rentre un chemin vers un fichier qui n'existe pas sur le disque
   <Le fichier est introuvable.>
2. Gérer l'erreur qui arrive quand Python n'arrive pas à lire le contenu du fichier qui est passé par l'utilisateur
   <Impossible d'ouvrir le fichier.>
3. Sinon lire le contenu du fichier et l'afficher à l'écran.
"""

fichier = input("Entrez le chemin d'un fichier à ouvrir : ")

try:
    fichier_ouvert = open(fichier, 'r')
except FileNotFoundError:
    print("Le fichier est introuvable.")
else:
    try:
        print(fichier_ouvert.read())
        fichier_ouvert.close()
    except:
        print("Impossible d'ouvrir le fichier.")