import sys
sys.path.append(".")
from flask import Flask
from src.web import plano 

app = Flask(__name__)
app.register_blueprint(plano.blueprint)


if __name__ == "__main__":
    app.run()