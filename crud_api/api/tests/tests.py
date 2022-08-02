import unittest
from crud_api.app import create_app


class TestGet(unittest.TestCase):
    def test_get_user_by_email(self):
        """Create a user and search for it,
        check if the json is equal the expected response."""
        tester = create_app().test_client(self)

        tester.post(
            'http://localhost:5000/crud?name=Elliot Anderson&email=black.hat666@protonmail.com')

        get_new_user = tester.get(
            'http://localhost:5000/crud?email=black.hat666@protonmail.com')

        self.assertEqual(
            get_new_user.data, b'{"email":"black.hat666@protonmail.com","id":1,"username":"Elliot Anderson"}\n')


if __name__ == '__main__':
    unittest.main()
