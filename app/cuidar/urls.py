from django.urls import path, include
from rest_framework import routers


# Views
from app.cuidar import views as cuidar_views


# InAuth
router = routers.DefaultRouter()
router.register('paciente', cuidar_views.PacienteViwerSet)
router.register('medicamento', cuidar_views.MedicamentoViwerSet)
router.register('patologia', cuidar_views.PatologiaViwerSet)



# NotAuth
urlpatterns = [
    path('cuidar/', include(router.urls)),
]
