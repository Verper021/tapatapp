import unittest
from flask import Flask
from prototipo1.servey2correcto import app, daoUser, User

class TestServey2Correcto(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "Hello World")

    def test_get_user_found(self):
        response = self.app.get('/user/usuari')
        self.assertEqual(response.status_code, 200)
        self.assertIn('usuari', response.data.decode('utf-8'))

    def test_get_user_not_found(self):
        response = self.app.get('/user/notfound')
        self.assertEqual(response.status_code, 404)
        self.assertIn('User not found', response.data.decode('utf-8'))

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIn('usuari', response.data.decode('utf-8'))
        self.assertIn('user2', response.data.decode('utf-8'))
        self.assertIn('admin', response.data.decode('utf-8'))

    def test_create_user(self):
        new_user = {
            'username': 'newuser',
            'password': 'newpassword',
            'email': 'newuser@example.com'
        }
        response = self.app.post('/user', json=new_user)
        self.assertEqual(response.status_code, 201)
        self.assertIn('newuser', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()