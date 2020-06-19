# Demander à l'utilisateur d'entrer un nombre
# Afficher le résultat de l'addition de ce nombre avec le nombre a.
# Par exemple : "Le résultat de l'opération est 15" (dans le cas où l'utilisateur entre le nombre 5)

a = 10
nombre = int(input("entrer un nombre: "))

print(f"la somme de {nombre} et a={a} est {a + nombre}")