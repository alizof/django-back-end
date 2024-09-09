# Libs
from django.db import models
import uuid

# Cliente
class Cliente(models.Model):

    TIPO_CHOICES = {
        "F": "Fisica",
        "J": "Juridica"
    }
    
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
    )

    nome = models.CharField(max_length=150,null=False)
    cip =  models.CharField(max_length=17,null=False)
    tipo = models.CharField(max_length=1,choices=TIPO_CHOICES,null=False,default="F")
    created_at = models.DateField(auto_now=True)

    
# Modelos  
class Modelo(models.Model):
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
    )
    nome = models.CharField(max_length=50,null=False)
    created_at = models.DateField(auto_now=True,editable=False)
    
# Produto   
class Produto(models.Model):
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
        )
    nome = models.CharField(max_length=100, null=False)
    unidade = models.CharField(max_length=30, null=False)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateField(auto_now=True)
    
# Fonecedor  
class Fonecedor(models.Model):
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
        )
    nome = models.CharField(max_length=40,null=False)
    cip = models.CharField(max_length=17,null=False)
    created_at = models.DateField(auto_now=True)