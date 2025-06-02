N_majuscules = 0
N_minuscules = 0
N_chiffres = 0
N_caracteres_speciaux = 0
pwd = input("Entrez un mot de passe : ")
if len(pwd) > 12 :
    for letter in pwd:
        if letter.isupper(): N_majuscules += 1
        if letter.islower(): N_minuscules += 1  
        if letter.isdigit(): N_chiffres += 1
        if letter in ['!', '@', '#', '$', '%', '^', '&', '*']: N_caracteres_speciaux += 1
    if N_majuscules > 0 and N_minuscules > 0 and N_chiffres > 0 and N_caracteres_speciaux > 0:
        print("Mot de passe valide.")

else:
    print("Le mot de passe doit contenir au moins 12 caractères.")

import random
import string
import re

def generer_mot_de_passe(longueur=12):
    if longueur < 12:
        raise ValueError("La longueur minimale est 12 caractères.")
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
    while True:
        mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
        # Vérifie avec une expression régulière la présence d'au moins une majuscule, minuscule, chiffre et caractère spécial
        if (re.search(r'[A-Z]', mot_de_passe) and
            re.search(r'[a-z]', mot_de_passe) and
            re.search(r'\d', mot_de_passe) and
            re.search(r'[!@#$%^&*]', mot_de_passe)):
            return mot_de_passe

# Exemple d'utilisation
print("Mot de passe généré :", generer_mot_de_passe(12))