import unittest
from flask import json
from main.main import app, listings

class TestListingsAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_all_listings(self):
        response = self.app.get('/listings')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(json.loads(response.get_data(as_text=True)), list))

    def test_get_listing_by_id(self):
        response = self.app.get('/listings/1')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(json.loads(response.get_data(as_text=True)), dict))

    def test_get_listings_by_query(self):
        response = self.app.get('/listings?neighborhood=Downtown')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(json.loads(response.get_data(as_text=True)), list))

    def test_create_listing(self):
        new_listing = {"name": "Test Listing", "price": 150, "neighborhood": "Test Neighborhood"}
        response = self.app.post('/listings', json=new_listing)
        self.assertEqual(response.status_code, 201)

    def test_update_listing(self):
        existing_listing = listings[0]
        updated_data = {"price": 200}
        response = self.app.patch(f'/listings/{existing_listing["id"]}', json=updated_data)
        self.assertEqual(response.status_code, 200)

    def test_delete_listing(self):
        existing_listing = listings[0]
        response = self.app.delete(f'/listings/{existing_listing["id"]}')
        self.assertEqual(response.status_code, 200)
        self.assertTrue({"message": "Listing deleted successfully"} in json.loads(response.get_data(as_text=True)))

    def test_listing_not_found(self):
        response = self.app.get('/listings/999')
        self.assertEqual(response.status_code, 404)
        self.assertTrue({"error": "Listing not found"} in json.loads(response.get_data(as_text=True)))


if __name__ == '__main__':
    unittest.main()
