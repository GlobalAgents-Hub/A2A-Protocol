# send.py
import socket
import json

def send_interaction(ip, entities):
    PORT = 5050
    BUFFER = 1024

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, PORT))

    msg = {
        "type": "interaction",
        "entities": entities
    }

    client.send(json.dumps(msg).encode())
    response = client.recv(BUFFER)
    print("📡 Resposta do peer:", response.decode())

    client.close()

# Exemplo de uso
if __name__ == "__main__":
    send_interaction("127.0.0.1", ["Lyra", "Nova", "Orion"])
