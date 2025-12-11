from flask import request, jsonify
import subprocess, uuid, os
from app import app  

@app.route("/run-js", methods=["POST"])
def run_js():
    data = request.get_json()
    code = data.get("code", "")

    filename = f"temp_{uuid.uuid4()}.js"
    with open(filename, "w") as f:
        f.write(code)

    try:
        result = subprocess.run(
            ["docker", "run", "--rm", "-v", f"{os.getcwd()}:/app", "node:20-slim", "node", f"/app/{filename}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10
        )
        return jsonify({"output": result.stdout or result.stderr})
    except subprocess.TimeoutExpired:
        return jsonify({"output": "Execution timed out"}), 400
    finally:
        os.remove(filename)
