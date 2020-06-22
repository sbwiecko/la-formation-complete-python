"""
1. Parcourir chaque fichier et récupérer le numéro du compte bancaire 'Crédit Mutuel' ainsi que le numéro de sécurité sociale.
2. Afficher les deux numéros à la fin du script.
"""
import glob
import json

dossier = "./dossier_exemple/**" # os.path.dirname(__file__)
files = glob.glob(dossier, recursive=True)

# init pour éviter les erreurs en fin de script
numero_compte = None
numero_secu = None

for file in files:
    if "comptes_bancaires" in file:
        with open(file, 'r') as f:
            data_dict = json.load(f)
            numero_compte = data_dict.get("Credit Mutuel").get("Numero de compte")
            # manque ici une vérification de l'existance de la clé
            
    if "securite_sociale" in file:
        with open(file, 'r') as f:
            numero_secu = int(f.read().split(':')[1])

print(f"numéro de compte Crédit Mutuel : {numero_compte}")
print(f"numéro de sécurité sociale : {numero_secu}")