import unittest
import requests


class TestGet(unittest.TestCase):
    def test_endpoint(self):
        """Create a user and search for it,
        check if the json is equal the expected response."""

        requests.post(
            'http://localhost:5000/crud?name=Elliot Anderson&email=black.hat666@protonmail.com')

        get_new_user = requests.get('http://localhost:5000/crud?id=1')
        response = get_new_user.content

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.content == 'b{"email":"black.hat666@protonmail.com","id":1,"username":"Elliot Anderson"}\n')


if __name__ == '__main__':
    pass
