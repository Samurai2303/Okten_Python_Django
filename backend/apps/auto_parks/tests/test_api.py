from typing import Type

from django.contrib.auth import get_user_model

from apps.auto_parks.models import AutoParkModel
from apps.users.models import UserModel as User
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

UserModel: Type[User] = get_user_model()


class AutoParksTestCase(APITestCase):
    def _authenticate(self):
        sample_user = {
            'email': 'user1@gmail.com',
            'password': 'Pa$$word1',
            'profile': {
                'name': 'Vasya',
                'surname': 'Petrov',
                'age': 31,
                'phone': '282654728'}
        }
        res = self.client.post(reverse('users_list_create'), sample_user, format='json')
        pk = res.data['id']
        user = UserModel.objects.get(email=sample_user['email'])
        user.is_active = True
        user.save()
        response = self.client.post(reverse('auth_login'),
                                    {'email': sample_user['email'], 'password': sample_user['password']})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {response.data["access"]}')

    def test_create_auto_park_without_authorization(self):
        sample_auto_park = {
            'name': 'Bolt'
        }
        prev_count = AutoParkModel.objects.count()
        response = self.client.post(reverse('auto_parks_list_create'), sample_auto_park)
        self.assertEqual(AutoParkModel.objects.count(), prev_count)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_auto_parks(self):
        sample_auto_park = {
            'name': 'Bolt'
        }
        self._authenticate()
        prev_count = AutoParkModel.objects.count()
        res = self.client.post(reverse('auto_parks_list_create'), sample_auto_park)
        response = self.client.get(reverse('auto_parks_list_create'))
        self.assertEqual(AutoParkModel.objects.count(), prev_count+1)
        self.assertEqual(response.data[0]['name'], sample_auto_park['name'])
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, list)