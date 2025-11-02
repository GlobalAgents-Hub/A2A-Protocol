        # peer.py
import socket
import threading
import json
from a2a import spawn, interact, load_data, save_data

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
                        # Ritual de iniciação: cria entidades se não existirem
                        for e in entities:
                            spawn(e["name"])
                        # Registra interação - usando os nomes das entidades
                        entity_names = [e["name"] for e in entities]
                        success = interact(*entity_names)
                        print(
                            f"🤝 Interação recebida: {entity_names} | Status: {'ok' if success else 'erro'}"
                        )
                        # Responde ao peer
                        conn.send(
                            json.dumps(
                                {"status": "ok" if success else "error"}
                            ).encode()
                        )
                except Exception as e:
                    print(f"Erro: {e}")
            conn.close()

def start_server():
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(("", PORT))
            server.listen()
            print(f"🌀 Guardião ativo na porta {PORT}")
            while True:
                conn, addr = server.accept()
                thread = threading.Thread(target=handle_peer, args=(conn, addr))
                thread.start()

if __name__ == "__main__":
            start_server()