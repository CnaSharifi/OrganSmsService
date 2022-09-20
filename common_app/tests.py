from django.test import TestCase

from django.contrib.auth import get_user_model
User = get_user_model()

from common_app.models import City, State

# Create your tests here.
class APITestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='user_test',password='1234')
        #self.data = {'username':}

        return super().setUp()

    def test_api_city_list(self):
        response = self.client.get('/api/city/').json()
        self.assertEqual(len(response), City.objects.all().count())

        city_title_json = response[5]['title']
        city_title_model = City.objects.get(id=6).title
        self.assertEqual(city_title_json, city_title_model)
        

    def test_api_state_list(self):
        response = self.client.get('/api/state/').json()
        self.assertEqual(len(response), State.objects.all().count())

        state_title_json = response[5]['title']
        state_title_model = State.objects.get(id=6).title
        self.assertEqual(state_title_json, state_title_model)

    
    def test_api_cities_of_state_list(self):
        state_id = 10
        response = self.client.get(f'/api/city/{state_id}/').json()
        self.assertEqual(len(response), City.objects.filter(state=state_id).count())

        city_title_json = response[0]['title']
        city_title_model = City.objects.filter(state=state_id).first().title
        self.assertEqual(city_title_json, city_title_model)
        