from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, celular_invalido


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'

    def validate(self, dados):
        print(dados)
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError(
                {'cpf': 'O CPF deve ter um valor válido'})

        if nome_invalido(dados['nome']):
            raise serializers.ValidationError(
                {'nome': 'O nome só pode ter letras'})

        if celular_invalido(dados['celular']):
            raise serializers.ValidationError(
                {'celular': 'O celular deve conter 13 dígitos'})
        return dados


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []


class ListaMatriculaEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaMatriculaCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')

    class Meta:
        model = Matricula
        fields = ['estudante_nome']


class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'celular']
