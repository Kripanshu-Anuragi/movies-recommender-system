
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Blueprint import and register
    from .routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
