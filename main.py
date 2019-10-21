
# Ecrire en python le code (utilisant flask) permettant
# d'écouter sur le port 5000 et de répondre "Hello world"
# quand l'utilisateur se connecte dessus

from flask import Flask

APP = Flask(__name__)

@APP.route('/')
def index():
    return "Hello world !"

if __name__ == "__main__":
    APP.run(host="0.0.0.0")
