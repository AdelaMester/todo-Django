from django.test import TestCase

# Create your tests here.
class TestCases(TestCase):
    def test_ok(self):
        response = self.client.get('/')
        print("code: "+ str(response.status_code))
        self.assertEqual(response.status_code, 200)

