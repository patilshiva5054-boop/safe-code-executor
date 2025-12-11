from flask import Flask, request, jsonify
import subprocess
import uuid
import os

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run_code():
    data = request.get_json()
    code = data.get("code", "")

    # Save temporary script
    filename = f"temp_{uuid.uuid4()}.py"
    with open(filename, "w") as f:
        f.write(code)

    try:
        # Execute code inside Docker
        result = subprocess.run(
            ["docker", "run", "--rm", "-v", f"{os.getcwd()}:/app", "python:3.11-slim", "python", f"/app/{filename}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10
        )

        output = result.stdout or result.stderr
        return jsonify({"output": output})

    except subprocess.TimeoutExpired:
        return jsonify({"output": "Execution timed out"}), 400

    finally:
        os.remove(filename)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)

