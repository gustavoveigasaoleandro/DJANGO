from django.test import TestCase
from escola.models import Estudante, Curso


class TestFixtures(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_carregamento_da_fixture(self):
        """Testa se os dados da fixture foram carregados corretamente"""
        estudante = Estudante.objects.get(cpf='13123131313')
        curso = Curso.objects.get(pk=1)
        self.assertEqual(estudante.nome, 'Vini')
        self.assertEqual(curso.codigo, 'P001')
