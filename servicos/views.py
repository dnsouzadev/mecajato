from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import FormServico

# Create your views here.
def servicos(request):
    return JsonResponse({"servicos": "servicos"})


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
