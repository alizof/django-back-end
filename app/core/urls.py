from django.urls import path, include
from rest_framework import routers


# Views
from app.core import views as core_views


# InAuth
router = routers.DefaultRouter()
router.register('users',core_views.UserViwerSet)
router.register('cliente',core_views.ClienteViwerSet)
router.register('produto',core_views.ProdutoViwerSet)
router.register('modelo',core_views.ModeloViwerSet)
router.register('fornecedor',core_views.FornecedorViwerSer)


# NotAuth
urlpatterns = [
    path('api/', include(router.urls)),
]
