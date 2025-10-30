def spawn_agent(name, db):
  agent_id = f"{name}_{len(db)+1}"
  db[agent_id] = {"name": name, "zone": None}
  return agent_id
