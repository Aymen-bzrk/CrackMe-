import re

def est_ip_valide(ip):
    # Regex pour valider une adresse IPv4
    regex = re.compile(
        r'^('
        r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}'
        r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$'
    )
    return bool(regex.match(ip))

# Tests
ips1 = [
    "192.168.1.1",
    "102.0.65.5",
    "172.16.254.1",
    "10.0.0.255",
    "256.256.256.256",
    "192.168.1.",
    "abc.def.ghi.jkl",
    "192.168.1.01",
    "0.0.0.0"
]
# Lecture des IPs depuis le fichier "inputs.txt"
with open("TP2\inputs.txt", "r") as f:
    ips = [line.strip() for line in f if line.strip()]

for ip in ips:
    print(f"{ip} -> {'Valide' if est_ip_valide(ip) else 'Invalide'}")