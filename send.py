import socket
import json

def send_interaction(ip, port, entities):
    BUFFER = 4096

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))

    interaction = {
        "type": "interaction",
        "entities": entities
    }

    client.send(json.dumps(interaction).encode())
    response = json.loads(client.recv(BUFFER).decode())

    print("📡 Resposta do peer:", response)
    client.close()

# Entrada dinâmica
ip = input("🌐 IP do peer: ").strip()
port = int(input("🔌 Porta do peer: ").strip())
raw_entities = input("🔗 Entidades (separadas por vírgula): ").split(",")

# Transforma em lista de dicionários
entities = [{"type": "NPC", "name": name.strip()} for name in raw_entities]

send_interaction(ip, port, entities)
