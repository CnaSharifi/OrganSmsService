from django.test import TestCase

from django.contrib.auth import get_user_model
User = get_user_model()

from common_app.models import City, State

import random

# Create your tests here.
class ApiTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='user_test',password='1234')
        self.random_num = random.randint(1,10)
        #self.data = {'username':}

        return super().setUp()

    def test_api_city_list(self):
        response = self.client.get('/api/city/').json()
        self.assertEqual(len(response), City.objects.all().count())

        city_title_json = response[self.random_num]['title']
        city_title_model = City.objects.get(id= self.random_num + 1).title
        self.assertEqual(city_title_json, city_title_model)
        

    def test_api_state_list(self):
        response = self.client.get('/api/state/').json()
        self.assertEqual(len(response), State.objects.all().count())

        state_title_json = response[self.random_num]['title']
        state_title_model = State.objects.get(id= self.random_num + 1).title
        self.assertEqual(state_title_json, state_title_model)

    
    def test_api_cities_of_state_list(self):

        response = self.client.get(f'/api/city/{self.random_num}/').json()
        self.assertEqual(len(response), City.objects.filter(state= self.random_num).count())

        city_title_json = response[-1]['title']
        city_title_model = City.objects.filter(state=self.random_num).last().title
        self.assertEqual(city_title_json, city_title_model)
        