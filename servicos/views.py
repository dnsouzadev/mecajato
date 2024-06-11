from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render

from servicos.models import Servico
from .forms import FormServico

# Create your views here.
def novo_servico(request):
    if request.method == 'GET':
        form = FormServico()
        return render(request, "novo_servico.html", {"form": form})
    elif request.method == 'POST':
        form = FormServico(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "ok"})
        else:
            return render(request, "novo_servico.html", {"form": form})
    else:
        return render(request, "novo_servico.html", {"form": FormServico()})


def listar_servico(request):
    if request.method == 'GET':
        servico = Servico.objects.all()
        return render(request, "listar_servico.html", {"servicos": servico})


def servico(request, identificador):
    if request.method == 'GET':
        servico = get_object_or_404(Servico, identificador=identificador)
        return render(request, "servico.html", {"servico": servico})
    elif request.method == 'POST':
        servico = Servico.objects.get(identificador=identificador)
        servico.finalizado = True
        servico.save()
        return HttpResponseRedirect("/listar_servico/")
    else:
        return render(request, "servico.html", {"servico": Servico.objects.get(identificador=identificador)})
