from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )

    codigo = models.CharField(max_length=10, unique=True, validators=[
                              MinLengthValidator(3)])
    descricao = models.CharField(max_length=100, blank=False)
    nivel = models.CharField(max_length=1, choices=NIVEL,
                             blank=False, null=False, default='B')

    def __str__(self):
        return self.descricao


class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )

    estudante = models.ForeignKey(
        Estudante, on_delete=models.CASCADE, related_name='matriculas')

    curso = models.ForeignKey(
        Curso, on_delete=models.CASCADE, related_name='matriculas')

    periodo = models.CharField(max_length=1, choices=PERIODO,
                               blank=False, null=False, default='M')

    def __str__(self):
        return f'{self.estudante} - {self.curso}'
