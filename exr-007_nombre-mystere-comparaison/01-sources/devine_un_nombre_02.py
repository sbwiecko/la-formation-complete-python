nombre_mystere = 7
nombre_utilisateur = input("Quel est le nombre mystère ? ")

# Afficher à l'aide d'une structure conditionnelle si le nombre entré par l'utilisateur est plus grand,
# plus petit ou égal au nombre mystère.
if int(nombre_utilisateur) > nombre_mystere:
    print(f"le nombre mystère est plus petit que {nombre_utilisateur}")
elif int(nombre_utilisateur) < nombre_mystere:
    print(f"le nombre mystère est plus grand que {nombre_utilisateur}")
else:
    print(f"le nombre mystère est bien {nombre_utilisateur}!")