from flask import Flask, request, jsonify
from a2a import spawn, create_zone, interact, load_data

app = Flask(__name__)

@app.route("/spawn", methods=["POST"])
def api_spawn():
    name = request.json.get("name")
    if not name:
        return jsonify({"error": "Missing 'name'"}), 400
    success = spawn(name)
    return jsonify({"status": "ok" if success else "error", "entity": name})

@app.route("/zone", methods=["POST"])
def api_zone():
    name = request.json.get("name")
    if not name:
        return jsonify({"error": "Missing 'name'"}), 400
    success = create_zone(name)
    return jsonify({"status": "ok" if success else "error", "zone": name})

@app.route("/interact", methods=["POST"])
def api_interact():
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
    app.run(host="127.0.0.1", port=5000)
