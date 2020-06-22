# chemin = "/Users/thibh/dossier_test"
import os

# Itérez sur le dictionnaire 'd' afin de créer les dossiers 'Films', 'Employes' et 'Exercices' ainsi que leur sous-dossier.

d = {"Films":
		["Le seigneur des anneaux",
		"Harry Potter",
		"Moon",
		"Forrest Gump"],
	 "Employes":
	 	["Paul",
	 	"Pierre",
		"Marie"],
	 "Exercices":
	 	["les_variables",
	 	"les_fichiers",
		"les_boucles"]}

path = ".\\"

list_paths = [os.path.join(path, supfolder, folder) for supfolder in d for folder in d[supfolder]]
for path in list_paths: os.makedirs(path, exist_ok=True)
