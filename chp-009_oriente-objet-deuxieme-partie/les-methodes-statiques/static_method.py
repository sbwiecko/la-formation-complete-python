class Voiture:
    voiture_crees = 0
    def __init__(self, marque, vitesse, prix):
        Voiture.voiture_crees += 1
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix
    
    # méthode d'instance
    def method(self):
        pass

    # méthode de classe (Class methods don't need a class instance)
    @classmethod
    def lamborghini(cls): # cls points to the class, not the object instance
        return cls(marque="Lamborghini", vitesse=250, prix=200000)

    @classmethod
    def porsche(cls):
        return cls(marque="Porsche", vitesse=200, prix=180000)

    # méthode statique (They work like regular functions but belong to the class's namespace.)
    @staticmethod
    def afficher_nombre_voitures(): # can accept any parameters
        print(f"Vous avez {Voiture.voiture_crees} voitures dans votre garage.")

lambo = Voiture.lamborghini()
porsche = Voiture.porsche()
Voiture.afficher_nombre_voitures()