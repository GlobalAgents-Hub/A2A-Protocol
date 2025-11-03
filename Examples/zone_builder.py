# examples/zone_builder.py

import threading
from peer import start_server

# Portas para os peers da zona
ports = [5050, 5051, 5052]

# Inicia cada peer em uma thread
for port in ports:
    thread = threading.Thread(target=start_server, args=(port,))
    thread.start()

print("🌀 Zona simbólica ativada com múltiplos peers.")
print("🔗 Aguardando interações...")
# examples/zone_builder.py
