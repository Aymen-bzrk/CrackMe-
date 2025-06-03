import re
from collections import Counter
import matplotlib.pyplot as plt
import csv
import json

# Partie 1 – Analyse textuelle
failed_ips = []
success_ips = []

# Lecture du fichier auth.log et extraction des adresses IP
with open("TP2/auth.log", "r", encoding="utf-8") as f:
    for line in f:
        if "Failed password" in line:
            # Extraction de l'adresse IP (IPv4)
            match = re.search(r'(\d{1,3}(?:\.\d{1,3}){3})', line)
            if match:
                failed_ips.append(match.group(1))
        elif "Accepted password" in line:
            match = re.search(r'(\d{1,3}(?:\.\d{1,3}){3})', line)
            if match:
                success_ips.append(match.group(1))

# Compter les occurrences de chaque IP
failed_counts = Counter(failed_ips)
success_counts = Counter(success_ips)

# Afficher les IPs ayant généré
top_failed = failed_counts.most_common(5)
ips = [ip for ip, _ in top_failed]
counts = [count for _, count in top_failed]
success_for_top = [success_counts.get(ip, 0) for ip in ips]

# Export JSON
data_json = [
    {"IP": ip, "Echecs": fail, "Succes": succ}
    for ip, fail, succ in zip(ips, counts, success_for_top)
]
with open("TP2/ssh_stats.json", "w", encoding="utf-8") as jsonfile:
    json.dump(data_json, jsonfile, indent=4)


# Création du graphique
x = range(len(ips))
plt.bar(x, counts, width=0.4, label="Échecs", color='red', align='center')
plt.bar(x, success_for_top, width=0.4, label="Succès", color='green', align='edge')

plt.xticks(x, ips)
plt.xlabel("Adresse IP")
plt.ylabel("Nombre de tentatives")
plt.title("Top 5 IPs avec le plus d'échecs de connexion SSH")
plt.legend()
plt.tight_layout()
plt.show()