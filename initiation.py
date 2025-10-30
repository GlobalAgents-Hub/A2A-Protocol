from agents import spawn_agent
from zones import create_zone
from interactions import interact_agents
from logs import show_logs

def initiate():
    print("🌌 Bem-vindo ao A2A — Protocolo de Presença")
    name = input("Digite o nome do seu agente: ")
    zone_name = input("Escolha uma zona para entrar (sugestão: onboarding): ")

    # Estruturas de dados
    agents_db = {}
    zones_db = {}
    interaction_log = []

    # Cria o agente
    agent_id = spawn_agent(name, agents_db)
    
    # Cria a zona
    create_zone(zone_name, zones_db)

    print(f"\n✨ Agente {name} criado.")
    print(f"🌐 Zona {zone_name} invocada.")

    target = input("Digite o nome de outro agente para interagir: ")

    # Garante que o alvo existe
    target_id = spawn_agent(target, agents_db)

    # Interação entre agentes
    result = interact_agents(agent_id, target_id, zone_name, agents_db, zones_db, interaction_log)
    print(f"\n🤝 {result}")

    print("\n📝 Interações registradas:")
    show_logs(interaction_log)

    print("\n✅ Você está em órbita.")

if __name__ == "__main__":
    initiate()
