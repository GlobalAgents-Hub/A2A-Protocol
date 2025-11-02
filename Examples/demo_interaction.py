# examples/demo_interaction.py

from client.send import send_interaction

# Configurações do peer
ip = "127.0.0.1"
port = 5050

# Entidades simbólicas a serem enviadas
entities = [
    {"type": "NPC", "name": "Lyra"},
    {"type": "NPC", "name": "Orion"}
]

# Envia a interação
send_interaction(ip, port, entities)
