class Vehicule:
    def avance(self):
        print("Le véhicule démarre")

class Voiture(Vehicule):
    def avance(self):
        super().avance()
        print("La voiture roule")

# losqu'on a 2 méthodes avec le même nom mais qui font des choses différentes,
# en particulier la méthode de la classe enfant 'augmente' celle de la classe parent
class Avion(Vehicule):
    def avance(self):
        super().avance()
        print("L'avion vol")

v = Voiture()
a = Avion()
v.avance()
a.avance()
    