from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def servicos(request):
    return JsonResponse({"servicos": "servicos"})


def novo_servico(request):
    return render(request, "novo_servico.html")
