# TPs Python – Aforp - Bouzerkoune Aymen M2 IRS P37
Tps Python pour le cours de Python a l'Aforp pour la semaine du 02/06/2025 - 06/06/2025

## Tp 1 Crackme.py
Petit jeu en Python pour deviner un mot de passe faible.  
Le mot est choisi au hasard dans un fichier texte.
**Fonctions :**
- Limite d’essais  
- Indices (longueur, lettres communes, etc.)  
- Option "triche" pour afficher le mot  
- Historique des tentatives  

**Fichier requis :** `mots_de_passe.txt` (un mot par ligne)

**Exercice a part :** checkpassword.py compteur des Maj, Min, Num et charcteres spec dans un password


---

## Tp 2 IPcheckRE.py

Réalisation d’un petit TP Regex pour vérifier si une adresse IP est correcte (vérification de base via expression régulière).

**Bibliotheque requise :** `re` (`import re` en haut du code)

**Fichier requis :** `ips.txt` (une @ ip par ligne)


##  TP3 Analyse de logs SSH (auth.log)

Ce script analyse un fichier `auth.log` contenant des connexions SSH (réussies ou échouées).  
Il identifie les IPs les plus suspectes et affiche un graphique comparatif.

---

### Partie 1 – Analyse simple
- Lecture du fichier `auth.log`
- Extraction des IPs ayant généré des erreurs `Failed password`
- Affichage des 5 IPs les plus actives (tentatives échouées)

---

###  Partie 2 – Visualisation + Bonus
- Utilisation de `matplotlib` pour afficher un graphique
- Comparaison entre les IPs ayant **échoué** et celles ayant **réussi** (`Accepted password`)
- Visualisation claire en barres rouges (échecs) et vertes (réussites)

---

###  Fichier requis :
- `auth.log` : fichier contenant les logs SSH (format standard)

Remarque:

Assure-toi d’avoir installé matplotlib :
pip install matplotlib

---