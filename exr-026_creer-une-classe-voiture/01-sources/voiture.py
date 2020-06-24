"""
* Créez une classe voiture avec un attribut 'essence' qui est égal à 100.
* Créez une méthode 'afficher_reservoir' qui affiche le nombre de litres d'essence restant
  ('La voiture contient x litres d'essence').
* Créez une méthode 'roule' avec un paramètre km (kilomètre) qui va faire avancer la voiture
  et vider petit à petit le réservoir. On considère une consommation de 5L pour 100km, l'opération
  mathématique pour déterminer le nombre de litres d'essence nécessaire en fonction du nombre de
  kilomètres est donc : (km * 5) / 100. Puis afficher le nombre de litres restant.
* Si le réservoir est vide quand on essaie de rouler, afficher la phrase :
  'Vous n'avez plus d'essence, faites le plein !' et empêchez la voiture d'avancer.
* Si la jauge d'essence descend en dessous de 10L, affichez la phrase : 'Vous n'avez bientôt plus d'essence !'
* Créez une méthode 'faire_le_plein' qui remet le niveau d'essence à 100L et qui affiche
  la phrase 'Vous pouvez repartir !'
"""

class Voiture:
    def __init__(self):
        self.essence = 100 # quantité à l'instanciation
    
    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence} litres d'essence")
    
    def roule(self, km=1): # par défaut avance de 1 km
        # s'il n'y a plus d'essence on n'avance pas!
        if self.essence <= 0:
            self.essence = 0 # on peut pas avoir un négatif
            print("Vous n'avez plus d'essence, faites le plein !")
            return
        
        # si on passe en dessous de 10 L
        if self.essence < 10:
            print("Vous n'avez bientôt plus d'essence !")
            # mais on continue à rouler
        
        # on consomme de l'essence
        self.essence -= 5 * km / 100
        self.afficher_reservoir()
    
    def faire_le_plein(self):
        self.essence = 100
        print("Vous pouvez repartir !")