import sys
from traceback import print_tb
from django.test import TestCase

from user_management.forms import LoginModelForm

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your tests here.

class AthenticationTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='user_test',password='1234')
        self.login_post_data = {'username': 'user_test', 'password': '1234', 'captcha_0': 'dummy-valuee', 'captcha_1': 'PASSED'}

        return super().setUp()

    def test_true_login_inputs(self):
        
        response = self.client.post('/login/', data=self.login_post_data)
        self.assertEqual(response.status_code , 302)


    def test_wrong_login_inputs(self):
        self.login_post_data['username'] = 'user_TEST'
        response = self.client.post('/login/', data= self.login_post_data)
        self.assertEqual(response.status_code , 200)

        self.login_post_data['password'] = '1@345'
        response = self.client.post('/login/', data= self.login_post_data)
        self.assertEqual(response.status_code , 200)


    def test_wrong_login_captcha(self):
        self.login_post_data['captcha_1'] = 'XXXX'
        response = self.client.post('/login/', data= self.login_post_data)
        self.assertEqual(response.status_code , 200)




    
        
        
           
