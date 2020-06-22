import json

path = "./file.json"

with open(path, 'w') as f:
    json.dump({str(i): i for i in range(10)}, f, indent=4)

# utilisation des fichiers json pour sauvegarder les données dans leur structure
with open(path, 'r') as f:
    dico = json.load(f)
    print(dico)