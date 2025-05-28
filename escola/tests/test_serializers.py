from django.test import TestCase
from escola.models import Estudante
from escola.serializer import EstudanteSerializer


class EstudanteSerializerTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome='Teste de Modelo',
            email='testedemodelo@gmail.com',
            cpf='68195899056',
            data_nascimento='2023-02-02',
            celular='86 99999-9999'
        )

        self.serializer_estudante = EstudanteSerializer(
            instance=self.estudante
        )

    def test_verifica_campos_serializados_de_estudante(self):
        """Teste que verifica os campos serializados"""
        dados = self.serializer_estudante.data
        self.assertEqual(
            set(dados.keys()), set(['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']))

    def test_verifica_dados_serializados_de_estudante(self):
        """Teste que verifica os dados serializados"""
        dados = self.serializer_estudante.data
        self.assertEqual(dados['nome'], 'Teste de Modelo')
        self.assertEqual(dados['email'], 'testedemodelo@gmail.com')
        self.assertEqual(dados['cpf'], '68195899056')
        self.assertEqual(dados['data_nascimento'], '2023-02-02')
        self.assertEqual(dados['celular'], '86 99999-9999')
