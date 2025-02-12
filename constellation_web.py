from datetime import datetime

import yaml
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Load class names from YAML
with open("class_names.yaml", "r") as f:
    class_names = yaml.safe_load(f)["classes"]


@app.route("/")
def index():
    return render_template("index.html", class_names=class_names)


@app.route("/generate", methods=["POST"])
def generate_url():
    data = request.json
    project = data.get("project")
    milestone = data.get("milestone")
    path = data.get("path")
    timestamp = data.get("timestamp") or datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    base_url = "https://constellation.mit.edu/dashboard"
    url = f"{base_url}/ic{project}/m/{milestone}/{timestamp}"
    if path:
        url += f"/{path}"

    return jsonify({"url": url})


if __name__ == "__main__":
    app.run(debug=True)
