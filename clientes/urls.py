from django.urls import path
from .views import clientes, att_cliente

urlpatterns = [
    path('', clientes, name='clientes'),
    path('atualiza_cliente/', att_cliente, name='atualiza_cliente')
]
