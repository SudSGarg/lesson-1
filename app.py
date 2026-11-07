import os
from flask import Flask, jsonify, render_template

app = Flask(__name__)

ENVIRONMENT = os.getenv("APP_ENV", "Development")
PORT = int(os.getenv("PORT", 5555))

@app.route('/')
def home():
    return render_template("index.html", env=ENVIRONMENT)

@app.route('/health')
def health():
    return jsonify({"status": "healthy","environment": ENVIRONMENT}), 200

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=PORT,
        debug=True if ENVIRONMENT == "Development" else False
    )