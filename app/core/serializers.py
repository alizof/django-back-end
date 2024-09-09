from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Cliente, Produto, Modelo, Fonecedor

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'url', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop('password')
        return ret
    
class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Cliente
        fields = ['id', 'url', 'nome', 'cip', 'tipo',  'created_at']

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = ['id', 'url', 'nome']

class ProdutoSerializer(serializers.ModelSerializer):
    
    modelo = serializers.PrimaryKeyRelatedField(queryset=Modelo.objects.all())

    class Meta:
        model = Produto
        fields = ['id', 'url', 'nome', 'modelo', 'preco']
        
class FornecedorSerializar(serializers.ModelSerializer):
    
    class Meta:
        model = Fonecedor
        fields = ['id', 'url', 'nome', 'cip', 'created_at']
