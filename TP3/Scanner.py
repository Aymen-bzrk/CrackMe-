import socket
import argparse
import threading
import csv

def scan_port(ip, port, timeout, open_ports, closed_ports, verbose):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
                if verbose:
                    print(f"Port {port} ouvert")
            else:
                closed_ports.append(port)
                if verbose:
                    print(f"Port {port} fermé")
    except socket.gaierror:
        print(f"Adresse IP invalide : {ip}")

def scan_ports_threaded(ip, start_port, end_port, timeout=0.5, verbose=False):
    open_ports = []
    closed_ports = []
    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(ip, port, timeout, open_ports, closed_ports, verbose))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return sorted(open_ports), sorted(closed_ports)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mini-scanner de ports TCP (multithreadé)")
    parser.add_argument("--ip", required=True, help="Adresse IP à scanner")
    parser.add_argument("--start-port", type=int, required=True, help="Port de début")
    parser.add_argument("--end-port", type=int, required=True, help="Port de fin")
    parser.add_argument("--verbose", action="store_true", help="Afficher les ports fermés")
    parser.add_argument("--output", help="Fichier de sortie (txt ou csv)")
    args = parser.parse_args()

    print(f"Scan de {args.ip} du port {args.start_port} au port {args.end_port}...")

    open_ports, closed_ports = scan_ports_threaded(args.ip, args.start_port, args.end_port, verbose=args.verbose)

    if open_ports:
        print("Ports ouverts :")
        for port in open_ports:
            print(port)
    else:
        print("Aucun port ouvert trouvé dans cette plage.")

    # Sauvegarde des résultats
    if args.output:
        if args.output.endswith(".csv"):
            with open(args.output, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Port", "Etat"])
                for port in open_ports:
                    writer.writerow([port, "ouvert"])
                for port in closed_ports:
                    writer.writerow([port, "fermé"])
            print(f"Résultats sauvegardés dans {args.output}")
        else:
            with open(args.output, "w") as f:
                f.write("Ports ouverts :\n")
                for port in open_ports:
                    f.write(f"{port}\n")
                if args.verbose:
                    f.write("\nPorts fermés :\n")
                    for port in closed_ports:
                        f.write(f"{port}\n")
            print(f"Résultats sauvegardés dans {args.output}")