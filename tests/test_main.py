from http import HTTPStatus


def test_it_returns_correct_message_on_index_page(app):
    with app.test_client() as c:
        response = c.get("/", follow_redirects=True)
        if response.status_code != HTTPStatus.OK:
            raise AssertionError(f"Expected HTTPStatus.OK, got {response.status_code}")


        expected_msg = "Hello from PSPDFKit Engineer"
        if response.text != expected_msg:
            raise AssertionError(f"Did not return correct welcome message. Got {response.text}, expected: {expected_msg}")


def test_health_status_for_k8(app):
    with app.test_client() as c:
        response = c.get("/health", follow_redirects=True)
        if response.status_code != HTTPStatus.OK:
            raise AssertionError(f"Expected HTTPStatus.OK for health check, got {response.status_code}")
