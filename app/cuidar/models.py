# Libs
from django.db import models
import uuid



# Paciente
class Paciente(models.Model):
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
    )

    GENERO_CHOICES = {
        "": "",
        "M": "Masculino",
        "F": "Feminino"
    }

    TIPO_SANGUE_CHOICES = {
        ""      : "",
        "A+"    : "A+",
        "A-"    : "A-",
        "B+"    : "B+",
        "B-"    : "B-",
        "AB+"   : "AB+",
        "AB-"   : "AB-",
        "O+": "O+",
        "O-"    : "O-"
    }

    nome           = models.CharField(max_length=150,null=False)
    informacoes    = models.TextField(default='')
    cpf            =  models.CharField(max_length=17,null=False)
    tipoSanguineo  = models.CharField(max_length=3,null=False, blank=False, choices=TIPO_SANGUE_CHOICES, default='')
    genero          = models.CharField(max_length=1,null=False, blank=False, choices=GENERO_CHOICES, default='')
    nacimento      = models.DateField(null=False)
    created_at     = models.DateField(auto_now=True)

# Medicamentos
class Medicamento(models.Model):
    DIAS_DA_SEMANA = [
        ('SEG', 'Segunda-feira'),
        ('TER', 'Terça-feira'),
        ('QUA', 'Quarta-feira'),
        ('QUI', 'Quinta-feira'),
        ('SEX', 'Sexta-feira'),
        ('SAB', 'Sábado'),
        ('DOM', 'Domingo'),
    ]
    
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
    )

    nome        = models.CharField(max_length=150,null=False)
    dia = models.CharField(max_length=3, choices=DIAS_DA_SEMANA, default='')
    descricao   = models.TextField(default="", blank=False)
    pacientes   = models.ManyToManyField(Paciente, related_name='medicamentos')
    created_at  = models.DateField(auto_now=True)

# Patologia
class Patologia(models.Model):
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
    )

    nome        = models.CharField(max_length=150,null=False)
    descricao   = models.TextField(default="", blank=False) 
    paciente    = models.ManyToManyField(Paciente, related_name='patologias')
    created_at  = models.DateField(auto_now=True)
