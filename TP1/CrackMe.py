import random

# Liste des mots de passe faibles
mots_de_passe_faibles = [
    "123456", "password", "admin", "123456789", "qwerty",
    "abc123", "letmein", "welcome", "monkey", "football"
]

mot_secret = random.choice(mots_de_passe_faibles)
historique = []

# Bonus : demander la limite d'essais
limite = input("Nombre maximum d'essais (laisser vide pour illimité) : ")
limite = int(limite) if limite.isdigit() else None

print('Tapez "triche" pour révéler le mot de passe (test).')

trouve = False
essais = 0

while not trouve:
    tentative = input("Devinez le mot de passe : ")
    historique.append(tentative)
    essais += 1

    if tentative == "triche":
        print(f"Le mot de passe est : {mot_secret}")
        continue

    if tentative == mot_secret:
        print(f"Bravo ! Mot de passe trouvé en {essais} essais.")
        break

    # Indices
    if len(tentative) < len(mot_secret):
        print("Le mot de passe est plus long.")
    elif len(tentative) > len(mot_secret):
        print("Le mot de passe est plus court.")
    elif tentative and tentative[0] == mot_secret[0]:
        print("Le mot de passe commence par la même lettre.")
    else:
        lettres_communes = len(set(tentative) & set(mot_secret))
        print(f"Nombre de lettres communes : {lettres_communes}")

    if limite and essais >= limite:
        print(f"Nombre maximum d'essais atteint. Le mot était : {mot_secret}")
        break

print("Historique des tentatives :", historique)