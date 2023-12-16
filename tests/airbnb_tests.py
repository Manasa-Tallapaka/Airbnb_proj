# tests/airbnb_tests.py

import sys
sys.path.append('C:\\Users\\talla\\Downloads\\airbnb_proj')

import unittest
from main.main import main

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.client = main.test_client()
        # Propagate exceptions to the test client
        self.client.testing = True

    def test_hello_endpoint(self):
        # Send a GET request to the '/' endpoint
        response = self.client.get('/')
        
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the response data contains the expected message
        self.assertIn(b'Hello, World!', response.data)

if __name__ == '__main__':
    unittest.main()
