import os
from flask import Flask

app = Flask(__name__)

# E6 : message configurable par variable d'environnement
MESSAGE = os.environ.get("APP_MESSAGE", "Bonjour depuis Docker !")

@app.route("/")
def index():
    return MESSAGE

if __name__ == "__main__":
    # E5 : 0.0.0.0 = écouter sur toutes les interfaces du conteneur
    app.run(host="0.0.0.0", port=5000)
