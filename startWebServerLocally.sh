# A script to run the webserver quickly and optimise configuraiton for local build. Runs provided you are coming from the devcontainer
export FLASK_DEBUG="1"
poetry run flask run --host=127.0.0.1 --port 80
