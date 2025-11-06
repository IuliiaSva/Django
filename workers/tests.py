from multiprocessing.connection import Client

from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Worker
from inkflows import settings

User = get_user_model()

@classmethod
def setUpClass(cls):
    cls.User = User.objects.create_user(username='test', email='<EMAIL>', password='<PASSWORD>')
    cls.auth_client = Client()
    cls.auth_client.force_login(cls.User)

def setUpModel():
    Worker.objects.create(
        id=1,
        date_of_joining = (2025, 11, 5),
        skills='тестировщик',
    )
    Worker.objects.create(
        id=2,
        date_of_joining=(2025, 11, 4),
        skills='тестировщик',
    )
    Worker.objects.create(
        id=3,
        date_of_joining=(2025, 11, 3),
        skills='другое',
    )
    Worker.objects.create(
        id=4,
        date_of_joining=(2025, 11, 2),
        skills='разработчик',
    )
    Worker.objects.create(
        id=5,
        date_of_joining=(2025, 11, 1),
        skills='другое',
    )
@classmethod
def tearDownModel():
    Worker.objects.all().delete()
    User.objects.all().delete()

class TestRoutes(TestCase):
    def test_home_page(self):
        url = ''
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_worker_page(self):
        url = '/worker/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_worker(self):
        url = '/worker/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_worker_auth(self):
        url = '/worker/1/'
        response = self.auth_client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_worker_not_auth(self):
        login_url = settings.LOGIN_URL
        url = '/worker/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

class TestContext(TestCase):
    def test_home_page_positive(self):
        url = ''
        response = self.client.get(url)
        expected_objects = Worker.objects.filter(id__in=[1, 2, 3, 4])
        for object in expected_objects:
            with self.subTest (object=object):
              self.assertIn(object, response.context['object_list'])

    def test_home_page_negative(self):
        url = ''
        response = self.client.get(url)
        unexpected_objects = Worker.objects.get(id=5)
        self.assertNotIn(unexpected_objects, response.context['object_list'])

    def test_worker_page_positive(self):
        url = '/worker/'
        response = self.client.get(url)
        expected_objects = Worker.objects.filter(id__in=[1 ,2 ,3, 4])
        for object in expected_objects:
            with self.subTest(object=object):
              self.assertIn(object, response.context['object_list'])

    def test_worker(self):
        url = '/worker/1/'
        response = self.client.get(url)
        expected_object = Worker.objects.get(id=1)
        self.assertEqual(expected_object, response.context['object'])