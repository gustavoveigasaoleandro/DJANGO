from escola.models import Estudante, Curso, Matricula
from escola.serializer import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaCursoSerializer, ListaMatriculaEstudanteSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from escola.throttles import MatriculaAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all().order_by("id")
    # serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['nome']
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de cursos.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    """
    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de matrículas.

    Métodos HTTP Permitidos:
    - GET, POST

    Throttle Classes:
    - MatriculaAnonRateThrottle: limite de taxa para usuários anônimos.
    - UserRateThrottle: limite de taxa para usuários autenticados.
    """
    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ["get", "post"]


class ListaMatriculaEstudante(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Estudante
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Matricula.objects.none()
        queryset = Matricula.objects.filter(
            estudante_id=self.kwargs['pk']).order_by("id")
        return queryset

    serializer_class = ListaMatriculaEstudanteSerializer


class ListaMatriculaCurso(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Curso
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Matricula.objects.none()
        queryset = Matricula.objects.filter(
            curso_id=self.kwargs['pk']).order_by("id")
        return queryset

    serializer_class = ListaMatriculaCursoSerializer
