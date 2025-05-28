from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status


class AuthenticationTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='testuser',
            password='testpassword'
        )
        self.url = reverse('Estudantes-list')
        self.user.save()

    def test_authentication_success(self):
        """Testa a autenticação com credenciais corretas"""
        usuario = authenticate(username='testuser', password='testpassword')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)

    def test_authentication_failure(self):
        """Testa a autenticação com credenciais incorretas"""
        usuario = authenticate(username='erro', password='testpassword')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_requisicao_get_autorizada(self):
        """Testa uma requisição GET autorizada"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_nao_autorizada(self):
        """Testa uma requisição GET autorizada"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
