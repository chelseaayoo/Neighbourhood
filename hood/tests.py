from django.test import TestCase
from .models import neighbourhood,healthservices
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.
class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Arina = neighbourhood(neighbourhood='Arina')

    def test_instance(self):
        self.assertTrue(isinstance(self.Arina,neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.Arina.save_neighbourhood()
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.Arina.delete_neighbourhood('Arina')
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)

    

    