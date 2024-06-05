from django.urls import path
from .views import clientes

urlpatterns = [
    path('', clientes, name='clientes'),
]
