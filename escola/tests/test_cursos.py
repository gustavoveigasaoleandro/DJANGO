from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status


class CursosTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='testuser',
            password='testpassword'
        )
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.user)
