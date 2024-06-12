from django.shortcuts import render

from clientes.models import Carro, Cliente
from servicos.models import Servico

# Create your views here.
def home(request):
    servicos_feitos = Servico.objects.filter(finalizado=True)
    servicos_pendentes = Servico.objects.filter(finalizado=False)
    total_servicos = Servico.objects.all()
    servicos_count = Servico.objects.count()
    clientes_count = Cliente.objects.count()
    carros_count = Carro.objects.count()

    count_servicos_feitos = servicos_feitos.count()
    count_servicos_pendentes = servicos_pendentes.count()

    media_preco_servico = 0
    for servico in total_servicos:
        media_preco_servico += servico.preco_total()
    media_preco_servico = media_preco_servico / servicos_count


    context = {
        'servicos_feitos': count_servicos_feitos,
        'servicos_pendentes': count_servicos_pendentes,
        'servicos_count': servicos_count,
        'clientes_count': clientes_count,
        'carros_count': carros_count,
        'media_preco_servico': media_preco_servico
    }

    return render(request, 'index.html', context)
