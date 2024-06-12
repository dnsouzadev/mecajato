from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from clientes.models import Carro, Cliente
from servicos.models import Servico
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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
        'media_preco_servico': f'{media_preco_servico:.2f}'
    }

    return render(request, 'index.html', context)

def registro(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'register.html', {'form': form})


def login_view(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Falha no login!'
    return render(
        request, 'login.html', context={'form': form, 'message': message})


def logout_view(request):
    logout(request)
    return redirect('login')
