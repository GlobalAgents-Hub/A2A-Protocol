from agents import create_agent
from zones import create_zone
from interactions import interact
from logs import log_interaction

def initiate():
    print("🌌 Bem-vindo ao A2A — Protocolo de Presença")
    name = input("Digite o nome do seu agente: ")
    zone_name = input("Escolha uma zona para entrar: ")

    agent = create_agent(name)
    zone = create_zone(zone_name)

    print(f"\n✨ Agente {name} criado.")
    print(f"🌐 Zona {zone_name} invocada.")

    print("\nVocê pode agora interagir com outros agentes.")
    target = input("Digite o nome de outro agente para interagir: ")

    interact(name, target, zone_name)
    log_interaction(name, target, zone_name)

    print("\n📝 Interação registrada. Você está em órbita.")