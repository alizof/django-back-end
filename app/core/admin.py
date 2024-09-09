# Libs
from django.contrib import admin
from django.contrib.sessions.models import Session


# Models
from .models import Cliente, Produto, Modelo, Fonecedor

# Table
class ClienteAdmin(admin.ModelAdmin): 
    model = Cliente
    list_display = ['nome','cip','tipo','created_at']
    
class ProdutoAdmin(admin.ModelAdmin):
    model = Produto
    list_display = ['id','nome','unidade','modelo']
    

class ModeloAdmin(admin.ModelAdmin): 
    model = Modelo
    list_display = ['id','nome']
    


# Django
admin.site.register(Session)

# CoreAPP
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Modelo, ModeloAdmin)
admin.site.register(Fonecedor)





