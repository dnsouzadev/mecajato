from django.http import JsonResponse
from django.shortcuts import render
from .forms import FormServico

# Create your views here.
def servicos(request):
    return JsonResponse({"servicos": "servicos"})


def novo_servico(request):
    form = FormServico()
    return render(request, "novo_servico.html", {"form": form})
