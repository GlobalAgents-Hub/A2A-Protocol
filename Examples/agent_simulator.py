    # examples/agent_simulator.py
import time
import random
import sys
import os

    # Adiciona o diretório pai ao path para importar send
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from send import send_interaction

ip = "127.0.0.1"
port = 5050
agents = ["Lyra", "Orion", "Nova", "Kai", "Zeno"]

while True:
        pair = random.sample(agents, 2)
        entities = [{"type": "NPC", "name": name} for name in pair]
        print(f"🔁 Simulando interação entre: {pair[0]} e {pair[1]}")
        send_interaction(ip, port, entities)
        time.sleep(5)