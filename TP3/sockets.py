import socket
import argparse

def scan_ports(ip, start_port, end_port, timeout=0.5):
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                result = s.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
        except socket.gaierror:
            print(f"Adresse IP invalide : {ip}")
            break
        except Exception as e:
            print(f"Erreur sur le port {port} : {e}")
    return open_ports

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mini-scanner de ports TCP")
    parser.add_argument("--ip", required=True, help="Adresse IP à scanner")
    parser.add_argument("--start-port", type=int, required=True, help="Port de début")
    parser.add_argument("--end-port", type=int, required=True, help="Port de fin")
    args = parser.parse_args()

    print(f"Scan de {args.ip} du port {args.start_port} au port {args.end_port}...")
    ports = scan_ports(args.ip, args.start_port, args.end_port)
    if ports:
        print("Ports ouverts :")
        for port in ports:
            print(port)
    else:
        print("Aucun port ouvert trouvé dans cette plage.")