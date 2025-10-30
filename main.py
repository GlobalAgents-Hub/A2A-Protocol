import typer
import json
from pathlib import Path
from typing import Optional
from datetime import datetime

app = typer.Typer()

DATA_FILE = Path("data.json")

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"entities": {}, "zones": {}, "interactions": [], "logs": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_log(message: str):
    data = load_data()
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "message": message
    }
    data["logs"].append(log_entry)
    save_data(data)

@app.command()
def spawn(name: str):
    """Spawn a new entity"""
    data = load_data()
    
    if name in data["entities"]:
        typer.echo(f"❌ Entity '{name}' already exists!")
        return
    
    data["entities"][name] = {
        "name": name,
        "created_at": datetime.now().isoformat(),
        "zone": None
    }
    save_data(data)
    add_log(f"Spawned entity: {name}")
    typer.echo(f"✨ Spawned entity: {name}")

@app.command()
def zone(name: str):
    """Create a new zone"""
    data = load_data()
    
    if name in data["zones"]:
        typer.echo(f"❌ Zone '{name}' already exists!")
        return
    
    data["zones"][name] = {
        "name": name,
        "created_at": datetime.now().isoformat(),
        "entities": []
    }
    save_data(data)
    add_log(f"Created zone: {name}")
    typer.echo(f"🌍 Created zone: {name}")

@app.command()
def interact(entity1: str, entity2: str, entity3: str):
    """Make entities interact"""
    data = load_data()
    
    entities = [entity1, entity2, entity3]
    missing = [e for e in entities if e not in data["entities"]]
    
    if missing:
        typer.echo(f"❌ Unknown entities: {', '.join(missing)}")
        return
    
    interaction = {
        "timestamp": datetime.now().isoformat(),
        "entities": entities
    }
    data["interactions"].append(interaction)
    save_data(data)
    add_log(f"Interaction: {entity1} ↔ {entity2} ↔ {entity3}")
    typer.echo(f"🤝 Interaction recorded: {entity1} ↔ {entity2} ↔ {entity3}")

@app.command()
def log():
    """Display all logs"""
    data = load_data()
    
    if not data["logs"]:
        typer.echo("📝 No logs yet")
        return
    
    typer.echo("📝 System Logs:")
    typer.echo("=" * 50)
    for entry in data["logs"]:
        timestamp = entry["timestamp"]
        message = entry["message"]
        typer.echo(f"[{timestamp}] {message}")

@app.command()
def demo():
    """Run a complete demo"""
    typer.echo("🎬 Running demo...\n")
    
    # Clear existing data for demo
    save_data({"entities": {}, "zones": {}, "interactions": [], "logs": []})
    
    # Demo sequence
    typer.echo("Step 1: Spawning entities...")
    spawn("Orion")
    spawn("Nova")
    spawn("Lyra")
    
    typer.echo("\nStep 2: Creating zones...")
    zone("Lyra")
    zone("Cosmos")
    
    typer.echo("\nStep 3: Interaction...")
    interact("Orion", "Nova", "Lyra")
    
    typer.echo("\nStep 4: Showing logs...")
    log()
    
    typer.echo("\n✅ Demo complete!")

if __name__ == "__main__":
    app()
