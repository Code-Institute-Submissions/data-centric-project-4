import unittest
from app import app
app.config['TESTING'] = True

class FlaskTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        self.client = app.test_client()
    
    def test_can_fetch_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
    
    def test_can_fetch_layout(self):
        response = self.client.get('/layout')
        self.assertEqual(response.status_code,200)
    
    def test_can_fetch_home(self):
        response = self.client.get('/base')
        self.assertEqual(response.status_code,200)
    
    def test_fetching_invalid_route_results_in_not_found(self):
        response =self.client.get('/xyxyyx')
        self.assertEqual(response.status_code,404)
    
    def test_can_get_testing(self):
        response = self.client.get('/testing')
        self.assertEqual(response.data,b'testing')

if __name__ == '__main__':
    unittest.main()