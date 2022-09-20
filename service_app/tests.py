from django.test import TestCase

from django.contrib.auth import get_user_model
User = get_user_model()

from common_app.models import City, State

from service_app.models import ServiceModel

# Create your tests here.

class ServiceTestCase(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='user_test',password='1234')
        self.state = State.objects.create(title = "Mazandaran")
        self.city = City.objects.create(title="Saari", state= self.state)
 

    def test_service_post_message(self):

        self.assertEqual(ServiceModel.objects.all().count(), 0)

        data = {"city" : self.city.id , "content" : "Message is sent !"}
        response=self.client.post( '/service/services/' , data)
        self.assertEqual(response.status_code , 201)

        self.assertEqual(ServiceModel.objects.all().count(), 1)
