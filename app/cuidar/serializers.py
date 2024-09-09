from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Paciente, Medicamento, Patologia



class MedicamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicamento
        fields = ['id', 'url', 'nome', 'descricao', 'created_at']


class PatologiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patologia
        fields = ['id', 'url', 'nome', 'descricao', 'paciente', 'created_at']


class PacienteSerializer(serializers.ModelSerializer):
    
    patologias = PatologiaSerializer(many=True, read_only=True)

    class Meta:
        model = Paciente
        fields = ['id', 'url', 'nome', 'cpf', 'nacimento', 'created_at', 'informacoes', 'tipoSanguineo', 'genero', 'patologias']
