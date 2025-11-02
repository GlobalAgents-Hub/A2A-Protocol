from flask import Flask, request, jsonify
from a2a import spawn, create_zone, interact, load_data

app = Flask(__name__)

# Rota raiz com informações da API
@app.route("/", methods=["GET"])
def api_info():
    return jsonify({
        "api": "A2A Global Agent API",
        "version": "1.0",
        "endpoints": {
            "/spawn": "POST - Create entity (requires 'name')",
            "/zone": "POST - Create zone (requires 'name')",
            "/interact": "POST - Register interaction (requires 'entities' array with 3 items)",
            "/log": "GET - Retrieve logs"
        }
    })

@app.route("/spawn", methods=["POST"])
def api_spawn():
    # Validação de JSON
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400

    name = request.json.get("name")
    if not name:
        return jsonify({"error": "Missing 'name'"}), 400

    success = spawn(name)
    return jsonify({"status": "ok" if success else "error", "entity": name})

@app.route("/zone", methods=["POST"])
def api_zone():
    # Validação de JSON
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400

    name = request.json.get("name")
    if not name:
        return jsonify({"error": "Missing 'name'"}), 400

    success = create_zone(name)
    return jsonify({"status": "ok" if success else "error", "zone": name})

@app.route("/interact", methods=["POST"])
def api_interact():
    # Validação de JSON
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400

    entities = request.json.get("entities")
    if not entities or len(entities) != 3:
        return jsonify({"error": "Provide exactly 3 entities"}), 400

    success = interact(*entities)
    return jsonify({"status": "ok" if success else "error", "entities": entities})

@app.route("/log", methods=["GET"])
def api_log():
    data = load_data()
    return jsonify({"logs": data.get("logs", [])})

if __name__ == "__main__":
    # Debug mode para desenvolvimento
    app.run(host="0.0.0.0", port=5000, debug=True)