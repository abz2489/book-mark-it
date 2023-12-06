from urllib import response
from django.test import TestCase
from django.urls import reverse

# Create your tests here.
# Views tests
class TestIndex(TestCase):
    """Testing index view"""

    def test_url(self):
        """Test if the URL, response and template used"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")  
