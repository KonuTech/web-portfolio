import os
from flask import Flask
from portfolio.routes import pages


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw")

    app.register_blueprint(pages)

    return app
