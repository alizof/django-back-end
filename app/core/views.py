# Libs
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from rest_framework import status
from rest_framework import filters


from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# Modules/Serializer
from .serializers import UserSerializer, ClienteSerializer, ProdutoSerializer, ModeloSerializer, FornecedorSerializar
from .models import Cliente, Produto, Modelo, Fonecedor

# Utils
from utils.views_pagination import Pagination
from utils.views_model_viewset import PouiViewSet



class UserViwerSet(PouiViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends     = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields    = ['username', 'email']
    search_fields       = ['username', 'email']
    viwer_name = 'Usuario'
    

class ClienteViwerSet(PouiViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    pagination_class = Pagination.DefaultPagination
    filter_backends     = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields    = ['cip', 'nome']
    search_fields       = ['cip', 'nome']
    #permission_classes = [permissions.IsAuthenticated]
    viwer_name = 'Cliente'
    
class ProdutoViwerSet(PouiViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    pagination_class = Pagination.DefaultPagination
    filter_backends     = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields    = ['modelo', 'nome']
    search_fields       = ['modelo', 'nome']
    #permission_classes = [permissions.IsAuthenticated]
    viwer_name = 'Produto'
    
class ModeloViwerSet(PouiViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
    pagination_class = Pagination.DefaultPagination
    filter_backends     = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields    = ['nome']
    search_fields       = ['nome']
    #permission_classes = [permissions.IsAuthenticated]
    viwer_name = 'Modelo'
    
class FornecedorViwerSer(PouiViewSet):
    queryset = Fonecedor.objects.all()
    serializer_class    = FornecedorSerializar
    pagination_class    = Pagination.DefaultPagination
    filter_backends     = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields    = ['cip', 'nome']
    search_fields       = ['cip', 'nome']
    #permission_classes = [permissions.IsAuthenticated]
    viwer_name  = 'Fornecedor'