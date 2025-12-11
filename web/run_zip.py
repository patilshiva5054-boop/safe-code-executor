from flask import request, jsonify
import subprocess, os, uuid, zipfile, shutil
from app import app

@app.route("/run-zip", methods=["POST"])
def run_zip():
    file = request.files["file"]
    folder = f"code_{uuid.uuid4()}"
    os.mkdir(folder)

    zip_path = f"{folder}/code.zip"
    file.save(zip_path)

    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(folder)

    try:
        result = subprocess.run(
            ["docker", "run", "--rm", "-v", f"{os.getcwd()}/{folder}:/app", "python:3.11-slim", "python", "/app/main.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10
        )
        return jsonify({"output": result.stdout or result.stderr})
    except subprocess.TimeoutExpired:
        return jsonify({"output": "Timeout"}), 400
    finally:
        shutil.rmtree(folder)
