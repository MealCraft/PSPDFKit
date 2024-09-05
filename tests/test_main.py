from http import HTTPStatus


def test_it_returns_correct_message_on_index_page(app):
    with app.test_client() as c:
        response = c.get("/", follow_redirects=True)
        assert response.status_code == HTTPStatus.OK

    expected_msg = "Hello from PSPDFKit Engineer"
    assert response.text == expected_msg, \
        f"Did not return correct welcome message. Got {response.text}" \
        + f" expected: {expected_msg}"


def test_health_status_for_k8(app):
    with app.test_client() as c:
        response = c.get("/health", follow_redirects=True)
        assert response.status_code == HTTPStatus.OK
