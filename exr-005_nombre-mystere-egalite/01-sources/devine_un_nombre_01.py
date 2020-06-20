nombre_mystere = 7

# Demander à l'utilisateur de deviner le nombre.
try:
    nombre = int(input("deviner le nombre mystère: "))
# Afficher si le nombre entré par l'utilisateur est égal au nombre mystère.
    if nombre == nombre_mystere:
        print("c'est bien le nombre mystère!")
    else:
        print("réessayer...")
except ValueError:
    print("entrer un nombre entier")