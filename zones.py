def create_zone(name, db):
  db[name] = {"agents": []}

def list_zones(db):
  return list(db.keys())
