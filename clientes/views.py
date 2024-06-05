from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import re
from clientes.models import Carro, Cliente


# Create your views here.
def clientes(request):
    if request.method == 'GET':
        clientes_list = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes': clientes_list})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')

        cliente = Cliente.objects.filter(cpf=cpf)
        if cliente.exists():
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'cpf': cpf, 'carro': carros, 'placa': placas, 'ano': anos, 'carros': zip(carros, placas, anos), 'erro': 'CPF já cadastrado!'})

        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'cpf': cpf, 'carro': carros, 'placa': placas, 'ano': anos, 'carros': zip(carros, placas, anos), 'erro': 'Email inválido!'})

        cliente = Cliente(
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            cpf=cpf
        )

        cliente.save()

        for carro, placa, ano in zip(carros, placas, anos):
            car = Carro(
                carro=carro,
                placa=placa,
                ano=ano,
                cliente=cliente
            )
            car.save()

        return HttpResponse('Cliente cadastrado com sucesso!')


def att_cliente(request):
    if request.method == 'POST':
        id_cliente = request.POST.get('id_cliente')
        consultar = Cliente.objects.filter(id=id_cliente)
        if not consultar.exists():
            return JsonResponse({'status': False, 'mensagem': 'Cliente não encontrado!'})
        return JsonResponse({'status': True, 'nome': consultar[0].nome, 'sobrenome': consultar[0].sobrenome, 'email': consultar[0].email, 'cpf': consultar[0].cpf})
