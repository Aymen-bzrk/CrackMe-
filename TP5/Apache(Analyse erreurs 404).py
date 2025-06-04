import re
import pandas as pd
import matplotlib.pyplot as plt

# 1. Fonction pour parser une ligne du log Apache
def parse_log_line(line):
    log_pattern = re.compile(
        r'(?P<ip>\S+) \S+ \S+ \[(?P<datetime>[^\]]+)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d{3}) "(?P<user_agent>[^"]*)"'
    )
    match = log_pattern.match(line)
    if match:
        return match.groupdict()
    else:
        return None

# 2. Charger et parser le fichier access.log
def load_log_to_df(filepath):
    records = []
    with open(filepath, encoding="utf-8", errors="ignore") as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                records.append(parsed)
    df = pd.DataFrame(records)
    print("Aperçu du DataFrame :")
    print(df.head())
    print("Colonnes du DataFrame :", df.columns.tolist())
    return df

# 3. Filtrer les erreurs 404
def filter_404(df):
    df_404 = df[df['status'] == '404']
    print(f"Nombre d'erreurs 404 : {len(df_404)}")
    return df_404

# 4. Top 5 des IPs générant le plus d’erreurs 404
def top_5_ips(df_404):
    top_ips = df_404['ip'].value_counts().head(5)
    print("Top 5 IPs générant des erreurs 404 :")
    print(top_ips)
    return top_ips

# 5. Visualisation
def plot_top_ips(top_ips):
    plt.figure(figsize=(8,5))
    top_ips.plot(kind='bar', color='tomato')
    plt.title("Top 5 IPs générant des erreurs 404")
    plt.xlabel("Adresse IP")
    plt.ylabel("Nombre d'erreurs 404")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

# 6. Détection de bots
def detect_bots(df_404):
    bot_keywords = ['bot', 'crawler', 'spider']
    mask = df_404['user_agent'].str.lower().str.contains('|'.join(bot_keywords), na=False)
    bots_df = df_404[mask]
    print(f"Nombre d'erreurs 404 provenant de bots : {len(bots_df)}")
    print("Exemple d'IPs suspectes (bots) :")
    print(bots_df['ip'].value_counts().head())
    percent_bots = 100 * len(bots_df) / len(df_404) if len(df_404) > 0 else 0
    print(f"Pourcentage d'erreurs 404 provenant de bots : {percent_bots:.2f}%")
    return bots_df, percent_bots

# 7. Discussion des résultats
def discussion(top_ips, bots_df, percent_bots):
    print("\n--- Discussion ---")
    print("Les IPs générant le plus d'erreurs 404 sont probablement des scanners, des bots ou des utilisateurs mal configurés.")
    if percent_bots > 50:
        print("La majorité des erreurs 404 proviennent de bots. Il peut être pertinent de bloquer ou limiter ces IPs.")
    else:
        print("Une part significative des erreurs 404 provient d'utilisateurs humains ou d'autres sources.")
    print("Automatiser cette détection est possible via des scripts réguliers ou des outils de monitoring (fail2ban, etc.).")

# 8. Main
def main():
    log_path = "TP5/access.log"  # Assurez-vous que ce fichier est dans le dossier du script
    df = load_log_to_df(log_path)
    df_404 = filter_404(df)
    top_ips = top_5_ips(df_404)
    plot_top_ips(top_ips)
    bots_df, percent_bots = detect_bots(df_404)
    discussion(top_ips, bots_df, percent_bots)

if __name__ == "__main__":
    main()