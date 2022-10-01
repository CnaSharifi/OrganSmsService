from distutils.log import Log
import sys
from traceback import print_tb
from urllib import response
from django.test import TestCase

from user_management.forms import LoginModelForm

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your tests here.

class AthenticationTestCase(TestCase):
    
    def setUp(self):

        self.login_post_data = {'username': 'user_test', 'password': '1234', 'captcha_0': 'dummy-valuee', 'captcha_1': 'PASSED'}
        self.user_super = User.objects.create_user(username = "user_test", password="1234", is_staff=True, is_superuser=True )
        self.user_not_super = User.objects.create_user(username = "user_test2", password="qwerty")
        

    def test_correct_data_login_form(self):

        form = LoginModelForm(data = self.login_post_data)
        self.assertTrue(form.is_valid())

        self.client.login(username=self.login_post_data['username'], password=self.login_post_data['password']) 
        response=self.client.get('/service/app/')
        self.assertEqual(response.status_code, 200)  


    def test_wrong_data_login_form(self):

        self.login_post_data['username'] = 'userTEST'
        form = LoginModelForm(data= self.login_post_data)
        self.assertFalse(form.is_valid())

        self.login_post_data['username'] = 'user_test'
        self.login_post_data['password'] = '123abc'
        form = LoginModelForm(data= self.login_post_data)
        self.assertFalse(form.is_valid())


    def test_correct_data_login_form_NOT_superuser(self):

        form = LoginModelForm(data = self.login_post_data)
        self.assertTrue(form.is_valid())

        self.login_post_data['username'] = 'user_test2'
        self.login_post_data['password'] = 'qwerty'

        form = LoginModelForm(data = self.login_post_data)
        self.assertFalse(form.is_valid())

        response=self.client.get('/service/app/')
        self.assertEqual(response.status_code, 302)  


    def test_wrong_capthca_login_form(self):

        self.login_post_data['captcha_1'] = 'XYZX'
        form = LoginModelForm(data = self.login_post_data)
        self.assertFalse(form.is_valid())
        
        response = self.client.get('/service/app/')
        self.assertEqual(response.status_code, 302)  





    
        
        
           
