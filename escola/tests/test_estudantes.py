from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializer import EstudanteSerializer


class EstudantesTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']

    def setUp(self):
        """  self.user = User.objects.create_superuser(
            username='testuser',
            password='testpassword'
        ) """
        self.user = User.objects.get(username='gustavo')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.user)
        self.estudante_01 = Estudante.objects.get(pk=1)
        self.estudante_02 = Estudante.objects.get(pk=2)
        # self.estudante_01 = Estudante.objects.create(
        #     nome='Estudante UM',
        #     email="estudante01@email.com",
        #     cpf='431.537.100-90',
        #     data_nascimento='2023-02-02',
        #     celular='86 99999-9999'
        # )
        # self.estudante_02 = Estudante.objects.create(
        #     nome='Estudante DOIS',
        #     email="estudante02@email.com",
        #     cpf='216.144.070-53',
        #     data_nascimento='2023-02-02',
        #     celular='86 99999-9999'
        # )

    def test_requisicao_get_estudantes(self):
        """Testa uma requisição GET autorizada"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_um_estudante(self):
        """Testa uma requisição GET autorizada"""
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(id=1)
        dados_estudante_serializado = EstudanteSerializer(dados_estudante).data
        print(dados_estudante_serializado)
        self.assertEqual(response.data, dados_estudante_serializado)

    def test_requisicao_post_para_criar_um_estudante(self):
        """Testa uma requisição POST autorizada"""
        dados = {
            'nome': 'EstudanteTRES',
            'email': 'estudante3@email.com',
            'cpf': '17584860079',
            'data_nascimento': '2023-02-02',
            'celular': '86 99999-9999'
        }

        response = self.client.post('/estudantes/', dados)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_um_estudante(self):
        """Teste de requisição DELETE um estudante"""
        response = self.client.delete(f'{self.url}1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_um_estudante(self):

        dados = {
            'nome': 'EstudanteQUATRO',
            'email': 'estudante3@email.com',
            'cpf': '17584860079',
            'data_nascimento': '2023-02-02',
            'celular': '86 99999-9999'
        }

        response = self.client.put(f'{self.url}1/', dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
