import json

from flask import (
    Blueprint,
    jsonify,
    current_app,
)

bp = Blueprint("main", __name__)

# K8s needs a place where a return 200 is always true for probing and checking 'alive' status
@bp.route("/health")
def health_status_for_k8s():
    """
    Response code needed for 200 for kubernates to check that it's alive
    """
    return jsonify(success=True)

@bp.route("/")
def home_page():
    """
    returns index (home) page 
    """
    return "hello junte"
