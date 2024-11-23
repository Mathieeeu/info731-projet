# /scripts/proxy.py 

import socket
import threading

def handle_client_request(client_socket, addr):
    try:
        # Recevoir la requête du client
        print("[*] Request received from client")

        # Lire les données du client
        request = b''  # Initialisation de la variable request en bytes
        client_socket.settimeout(1.0)  # Définir un timeout pour éviter de bloquer indéfiniment

        while True:
            try:
                # Recevoir les données du client
                data = client_socket.recv(1024)
                if not data:
                    break
                request += data
                print(f"\033[96m[*] Received {len(data)} bytes\033[0m")
                # print(f"{data.decode('utf-8')}")
            except socket.timeout:
                break

        # Extraire l'hôte et le port de la requête
        host, port = extract_host_port_from_request(request)

        # Créer une socket pour se connecter au serveur distant
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as destination_socket:
            # Se connecter au serveur distant
            destination_socket.connect((host, port))
            destination_socket.settimeout(1.0)  # Définir un timeout pour la réception des données (car on attend toujours ce délai à la fin de la .recv())

            # Envoyer la requête au serveur distant
            destination_socket.sendall(request)

            # Recevoir la réponse du serveur distant
            print("[*] Response received from server")
            response = b''
            CHUNK_SIZE = 1024
            IS_LEGAL = True
            while True:
                try:
                    data = destination_socket.recv(CHUNK_SIZE)

                    if not data:
                        break

                    print(f"\033[96m[*] Received {len(data)} bytes\033[0m")
                    # print(f"{data.decode('utf-8')}")  # Afficher les données reçues

                    if isAllowed(data, addr[0]):
                        # Ajouter les données à la réponse
                        response += data
                    else:
                        body = b"<h1>403 Forbidden</h1>\r\n"
                        response = b"HTTP/1.1 403 Forbidden\r\nContent-Length: " + str(len(body)).encode() + b"\r\n\r\n" + body + b"\r\n"
                        IS_LEGAL = False
                        print("\033[91m[*] Blocked content detected - sending response to client\033[0m")
                        break

                except socket.timeout:
                    break
            if IS_LEGAL:
                print("\033[92m[*] Legal content detected - sending response to client\033[0m")
            # Envoyer la réponse au client
            client_socket.sendall(response)

    except Exception as e:
        print(f"\033[91m[*][*] Exception: {e}\033[0m")

    finally:
        # Fermer le socket du client
        client_socket.close()
        print(f"[*] Closing connection\n\n")

def extract_host_port_from_request(request):
    # Récupérer la valeur après l'entête "Host:"
    host_string_start = request.find(b"Host: ") + len(b"Host: ")
    host_string_end = request.find(b"\r\n", host_string_start)
    host_string = request[host_string_start:host_string_end].decode("utf-8")

    # Trouver la position du port
    webserver_pos = host_string.find("/")
    if webserver_pos == -1:  # Pas de port spécifié
        webserver_pos = len(host_string)
    port_pos = host_string.find(":")  # Position du port

    if port_pos == -1 or webserver_pos < port_pos:
        # Port par défaut
        port = 80
        host = host_string[:webserver_pos]
    else:
        # Extraire le port spécifié dans l'en-tête "Host:"
        port = int((host_string[(port_pos+1):])[:webserver_pos-port_pos-1])
        host = host_string[:port_pos]

    return host, port

def isAllowed(data,address):
    # Vérifier si le contenu est autorisé
    BAN_WORDS = ["jinx", "bonheur", "danger", "moved"]
    BYPASS_IPS = ["5.5.6.3","5.5.5.2"]

    if address in BYPASS_IPS: 
        print(f"\033[94m[*] Bypassing firewall for IP: {address}\033[0m")
        return True
    
    for word in BAN_WORDS:
        if word.encode() in data:
            print(f"\033[93m[*] Blocked content: word:{word} <---------\033[0m")
            return False
        
    return True

# Configuration du proxy
PROXY_HOST = "0.0.0.0"
PROXY_PORT = 8888

# Configuration du serveur
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Accepter jusqu'à 5 connexions entrantes
server.bind((PROXY_HOST, PROXY_PORT))
server.listen(5)
print(f"[*] Proxy listening on {PROXY_HOST}:{PROXY_PORT}")

while True:
    # Recevoir la requête du client
    client_socket, addr = server.accept()
    print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

    # Créer un thread pour gérer la connexion
    client_handler = threading.Thread(target=handle_client_request, args=(client_socket, addr))

    # Démarrer le thread
    client_handler.start()

# Pour tester le proxy, vous pouvez utiliser curl avec un proxy spécifié:
# curl --proxy <adresse_firewall>:8888 httpbin.org/ip   (on spécifie le proxy, on peut aussi mettre -x à la place de --proxy)
# curl httpbin.org/ip     (devrait marcher aussi)