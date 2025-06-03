import re
from collections import Counter

# Partie 1 – Analyse textuelle
failed_ips = []

with open("auth.log", "r", encoding="utf-8") as f:
    for line in f:
        if "Failed password" in line:
            # Extraction de l'adresse IP (IPv4)
            match = re.search(r'(\d{1,3}(?:\.\d{1,3}){3})', line)
            if match:
                failed_ips.append(match.group(1))

# Compter les occurrences de chaque IP
ip_counts = Counter(failed_ips)

# Afficher les 5 IPs ayant généré le plus d’échecs
print("Top 5 IPs avec le plus d'échecs de connexion SSH :")
for ip, count in ip_counts.most_common(5):
    print(f"{ip} : {count} échecs")