from django.test import TestCase

from django.contrib.auth import get_user_model
User = get_user_model()

from common_app.models import City, State


# Create your tests here.
class ApiTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='user_test',password='1234')

        self.state_test_1 = State.objects.create(title = "Esfahan")
        self.state_test_2 = State.objects.create(title = "Shiraz")
        
        self.city_test_1 = City.objects.create(title = "Baharestan", state= self.state_test_1)
        self.city_test_2 = City.objects.create(title = "KhomeiniShahr", state= self.state_test_1)
        self.city_test_3 = City.objects.create(title = "ShahinShahr", state=self.state_test_1)
        self.city_test_4 = City.objects.create(title = "Shiraz", state=self.state_test_2)
        self.city_test_5 = City.objects.create(title = "Abade", state=self.state_test_2)


    def test_api_city_list(self):
        response = self.client.get('/api/city/').json()
        self.assertEqual(len(response), City.objects.all().count())

        city_title_json = response[0]['title']
        city_title_model = City.objects.first().title
        self.assertEqual(city_title_json, city_title_model)
        

    def test_api_state_list(self):
        response = self.client.get('/api/state/').json()
        self.assertEqual(len(response), State.objects.all().count())

        state_title_json = response[0]['title']
        state_title_model = State.objects.first().title
        self.assertEqual(state_title_json, state_title_model)

    
    def test_api_cities_of_state_list(self):

        response = self.client.get(f'/api/city/?parent={self.city_test_1.id}').json()
        self.assertEqual(len(response), City.objects.filter(state= self.city_test_1.id).count())

        city_title_json = response[-1]['title']
        city_title_model = City.objects.filter(state=self.city_test_1.id).last().title
        self.assertEqual(city_title_json, city_title_model)
        