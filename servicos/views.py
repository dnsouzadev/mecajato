from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def servicos(request):
    return JsonResponse({"servicos": "servicos"})
