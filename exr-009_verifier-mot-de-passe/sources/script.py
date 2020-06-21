"""
1. Afficher la phrase mdp_trop_court en majuscule si le mot de passe entré est égal à 0.
2. Afficher la phrase mdp_trop_court avec une majuscule sur la première lettre si le mot de passe entré est plus petit que 8.
3. Afficher la phrase "Votre mot de passe ne contient que des nombres." si le mot de passe entré ne contient que des nombres.
4. Afficher la phrase "Inscription terminée." si le mot de passe est valide.
"""

mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."

if not len(mdp): print(mdp_trop_court.upper())
elif mdp.isdigit() : print("Votre mot de passe ne contient que des nombres.")
elif len(mdp) < 8: print(mdp_trop_court.capitalize())
else: print("Inscription terminée.")