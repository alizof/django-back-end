# Libs
from django.contrib import admin


# Models
from .models import Paciente, Medicamento, Patologia


# Table
class PacienteAdmin(admin.ModelAdmin): 
    model = Paciente
    list_display = ['nome', 'cpf', 'created_at']

class MedicamentoAdmin(admin.ModelAdmin): 
    model = Medicamento
    list_display = ['nome', 'descricao', 'created_at']

class PatologiaAdmin(admin.ModelAdmin): 
    model = Medicamento
    list_display = ['nome', 'descricao', 'created_at']




# App
admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Medicamento,MedicamentoAdmin)
admin.site.register(Patologia,PatologiaAdmin)
