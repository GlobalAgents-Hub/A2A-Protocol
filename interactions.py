def interact_agents(a1, a2, zone, agents, zones, log):
  if a1 not in agents or a2 not in agents:
      return "Agente não encontrado."
  if zone not in zones:
      return "Zona inexistente."
  log_entry = f"{a1} ↔ {a2} em {zone}"
  log.append(log_entry)
  return log_entry
