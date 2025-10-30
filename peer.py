# peer.py
import socket
import threading
import json
from a2a import interact

PORT = 5050
BUFFER = 1024

def handle_peer(conn, addr):
    print(f"🔗 Conectado com {addr}")
    while True:
        data = conn.recv(BUFFER)
        if not data:
            break
        try:
            msg = json.loads(data.decode())
            if msg["type"] == "interaction":
                entities = msg["entities"]
                interact(*entities)
                print(f"🤝 Interação recebida: {entities}")
        except Exception as e:
            print(f"Erro: {e}")
    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", PORT))
    server.listen()
    print(f"🌀 Aguardando conexões na porta {PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_peer, args=(conn, addr))
        thread.start()

def send_interaction(ip, entities):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, PORT))
    msg = json.dumps({"type": "interaction", "entities": entities})
    client.send(msg.encode())
    client.close()

if __name__ == "__main__":
    start_server()
