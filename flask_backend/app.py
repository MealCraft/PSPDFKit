from flask import (
    Blueprint,
    jsonify,
)

bp = Blueprint("main", __name__)


@bp.route("/health")
def health_status_for_k8s():
    """
    Response code needed for 200 for kubernates to check that it's alive
    """
    return jsonify(success=True)


@bp.route("/")
def home_page():
    """
    returns index (home) page.
    """
    return "Hello from PSPDFKit Engineer"
