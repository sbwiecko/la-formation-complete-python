projets = ["pr_GameOfThrones", "HarryPotter", "pr_Avengers"]
class Utilisateur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return f"Utilisateur {self.nom} {self.prenom}"

    def afficher_projets(self):
        for projet in projets:
            print(projet)

class Junior(Utilisateur):
    def __init__(self, nom, prenom):
        #Utilisateur.__init__(self, nom, prenom)
        super().__init__(nom, prenom) # accès à la fonction __init__ de la classe parent
                                      # super() sous-entend Utilisateur comme paramètre
                                      # mais pas de self passé en arg de __init__

paul = Junior("Paul", "Durand")
paul.afficher_projets()

