
from crud_api.app import create_app
import requests


def test_get():
    with create_app().app_context():
        test_request = requests.post(
            'www.localhost:5000?name=test_name&email=malicious.email666@gmail.com')
        assert test_request.status_code == 200


if __name__ == '__main__':
    test_get()
