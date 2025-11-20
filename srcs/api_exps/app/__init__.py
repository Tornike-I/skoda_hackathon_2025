from flask import Flask
from flask_cors import CORS
def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})


    # register blueprints
    from .routes.hello_routes import hello_bp

    app.register_blueprint(hello_bp, url_prefix="/api")

    return app
