from flask import Flask


def create_app(settings=None):
    """
    Creats the flask app with certain settings
    """
    flask_app = Flask(__name__)

    # Slashes at the end doesn't matter
    flask_app.url_map.strict_slashes = False

    from . import app
    flask_app.register_blueprint(app.bp)

    return flask_app


if __name__ == "__main__":
    app = create_app()
    app.run(
        host="127.0.0.1",
        port=80,
    )
