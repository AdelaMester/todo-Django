from django.test import TestCase
import unittest

# Create your tests here.

# '/' route tested
class test_index(TestCase):
    def test_ok(self):
        response = self.client.get('/')
        print("code: "+ str(response.status_code))
        self.assertEqual(response.status_code, 200)

# '/register' route tested
class test_register(TestCase):
    def test2(self):
        test_register = self.client.generic('POST', '/register', "username=abc&password=abc&confirmation=abc")
        self.assertEqual(test_register.status_code, 200)

