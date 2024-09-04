from flask import Flask
from . import app


def create_app(settings=None):
    """
    Creats the flask app with certain settings
    """
    flask_app = Flask(__name__)

    # Slashes at the end doesn't matter
    flask_app.url_map.strict_slashes = False

    flask_app.register_blueprint(app.bp)

    return flask_app


if __name__ == "__main__":
    app = create_app()
    app.run(
        host="0.0.0.0",
        port=80,
    )