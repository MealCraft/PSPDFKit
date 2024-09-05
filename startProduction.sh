# A script to run your webserver locally, provided you a running from the devcontainer
poetry run gunicorn "flask_backend:create_app()"
