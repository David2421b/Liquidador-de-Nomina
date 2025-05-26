
from flask import Flask
from web import plano 

app = Flask(__name__)
app.register_blueprint(plano.blueprint)


if __name__ == "__main__":
    app.run()