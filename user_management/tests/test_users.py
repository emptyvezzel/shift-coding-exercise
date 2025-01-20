import unittest
from app import create_app

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_get_users(self):
        response = self.client.get('/user_list')
        self.assertEqual(response.status_code, 200)

    def test_find_user(self):
        response = self.client.get('/find_user?name=Leanne')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()