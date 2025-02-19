import unittest
from seveeyp import app, DAOUsers, User
import json

class TestSeveeyp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.user_dao = DAOUsers()

    def test_get_user_by_username_success(self):
        response = self.app.get('/tapatapp/getuser?username=pare')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['username'], 'pare')
        self.assertEqual(data['email'], 'pare@gmail.com')

    def test_get_user_by_username_not_found(self):
        response = self.app.get('/tapatapp/getuser?username=nonexistent')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'User not found')

    def test_get_user_by_username_no_username(self):
        response = self.app.get('/tapatapp/getuser?username=')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'User not found')

if __name__ == '__main__':
    unittest.main()