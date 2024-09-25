import unittest
from app import app

class TestHiWorld(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hi_world(self):
        response = self.app.get('/')
        self.assertEqual(response.data, b'Hi, World!')