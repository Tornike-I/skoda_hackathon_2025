from flask import Flask
from flask_cors import CORS
from jinja2.utils import urlize


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})


    # register blueprints
    from .routes.hello_routes import hello_bp
    from .routes.course_fetcher_route import courses_bp
    app.register_blueprint(hello_bp, url_prefix="/api")
    app.register_blueprint(courses_bp, url_prefix="/api")

    return app
