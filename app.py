import os
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# This is an environment variable. We can use this later to teach them CI/CD config
ENVIRONMENT = os.getenv("APP_ENV", "DEVELOPMENT")
PORT = int(os.getenv("PORT", 5555))

# HTML Template stored as a string so they don't have to manage multiple files yet
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Training App</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f4f6f9; }
        .card { background: white; padding: 30px; display: inline-block; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; }
        .badge { background: #3498db; color: white; padding: 5px 10px; border-radius: 4px; font-size: 0.9em; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 DevOps Training Web App</h1>
        <p>Current Environment: <span class="badge">{{ env }}</span></p>
        <p>Status: <strong>Online & Running!</strong></p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, env=ENVIRONMENT)

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "environment": ENVIRONMENT}), 200

if __name__ == '__main__':
    # Listen on port 5555. Great for teaching network routing/ports later
    app.run(host='0.0.0.0', port=PORT, debug=True if ENVIRONMENT == "Development" else False)
 