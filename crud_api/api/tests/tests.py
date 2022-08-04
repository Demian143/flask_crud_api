import unittest
from crud_api.app import create_app

""" I need to: check if the right parameters is beeing passed"""


class TestGet(unittest.TestCase):
    tester = create_app().test_client()

    def test_get_user_by_email(self):
        """Create a user and search for by email,
        check if the json is equal the expected response."""
        self.tester.post(
            '/crud?name=Elliot Anderson&email=black.hat666@protonmail.com')

        get_new_user = self.tester.get(
            '/crud?email=black.hat666@protonmail.com')

        self.assertEqual(
            get_new_user.data, b'{"email":"black.hat666@protonmail.com","id":1,"username":"Elliot Anderson"}\n')

    def test_get_user_by_id(self):
        """Create a user and search by id,
        check if the json is equal the expected response."""
        self.tester.post(
            '/crud?name=Elliot Anderson&email=black.hat666@protonmail.com')

        get_new_user = self.tester.get(
            '/crud?id=1')

        self.assertEqual(
            get_new_user.data, b'{"email":"black.hat666@protonmail.com","id":1,"username":"Elliot Anderson"}\n')

    def test_get_unexisting_user(self):
        get_unexisting_user = self.tester.get('/crud?id=2')

        self.assertEqual(get_unexisting_user.data,
                         b'{"message":"user don\'t exists","status":400}\n')

    def test_passing_email_in_id(self):
        wrong_query = self.tester.get('/crud?id=black.hat666@protonmail.com')
        self.assertEqual(
            wrong_query.data, b'{"message":"You are maybe passing the wrong parameters in the request, please use the parameter \'id\' to search for a user","status":400}\n')


if __name__ == '__main__':
    unittest.main()
