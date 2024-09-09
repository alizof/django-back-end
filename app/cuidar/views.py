# Libs
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter


# Modules/Serializer
from .serializers import PacienteSerializer, MedicamentoSerializer, PatologiaSerializer
from .models import Paciente, Medicamento, Patologia

# Utils
from utils.views_pagination import Pagination
from utils.views_model_viewset import PouiViewSet


class PacienteFilter(FilterSet):
    cpf = CharFilter(field_name='cpf', lookup_expr='icontains')
    nome = CharFilter(field_name='nome', lookup_expr='icontains')

    class Meta:
        model = Paciente
        fields = ['cpf', 'nome']

class PacienteViwerSet(PouiViewSet):
    queryset            = Paciente.objects.all()
    serializer_class    = PacienteSerializer
    pagination_class    = Pagination.DefaultPagination
    filterset_class     = PacienteFilter
    filter_backends     = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields    = ['cpf', 'nome']
    search_fields       = ['cpf', 'nome']
    #permission_classes = [permissions.IsAuthenticated]
    viwer_name          = 'Paciente'

    


class MedicamentoViwerSet(PouiViewSet):
    queryset            = Medicamento.objects.all()
    serializer_class    = MedicamentoSerializer
    pagination_class    = Pagination.DefaultPagination
    filter_backends     = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields    = ['nome', 'descricao']
    search_fields       = ['nome', 'descricao']
    viwer_name          = 'Medicamento'

class PatologiaViwerSet(PouiViewSet):
    queryset            = Patologia.objects.all()
    serializer_class    = PatologiaSerializer
    pagination_class    = Pagination.DefaultPagination
    filter_backends     = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields    = ['nome', 'descricao']
    search_fields       = ['nome', 'descricao']
    viwer_name          = 'Patologia'

