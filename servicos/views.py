from io import BytesIO
import re
from django.http import FileResponse, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from fpdf import FPDF
from servicos.models import Servico, ServicoAdicional
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
    servico = get_object_or_404(Servico, identificador=identificador)
    return render(request, 'servico.html', {'servico': servico, 'servicos_adicionais': ServicoAdicional.objects.filter(servico=servico)})


def gerar_os(request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador)

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', 12)

    pdf.set_fill_color(240,240,240)
    pdf.cell(35, 10, 'Cliente:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.cliente.nome}', 1, 1, 'L', 1)

    pdf.cell(35, 10, 'Manutenções:', 1, 0, 'L', 1)

    categorias_manutencao = servico.categoria_manutencao.all()
    for i, manutencao in enumerate(categorias_manutencao):
        pdf.cell(0, 10, f'- {manutencao.get_titulo_display()}', 1, 1, 'L', 1)
        if not i == len(categorias_manutencao) -1:
            pdf.cell(35, 10, '', 0, 0)

    for servico_adicional in servico.servicos_adicionais.all():
        pdf.cell(35, 10, 'Serviço adicional:', 1, 0, 'L', 1)
        pdf.cell(0, 10, f'- {servico_adicional.titulo}', 1, 1, 'L', 1)

    pdf.cell(35, 10, 'Preco Total', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'R$ {servico.preco_total()}', 1, 1, 'L', 1)
    pdf.cell(35, 10, 'Data de início:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.data_inicio}', 1, 1, 'L', 1)
    pdf.cell(35, 10, 'Data de entrega:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.data_entrega}', 1, 1, 'L', 1)
    pdf.cell(35, 10, 'Protocolo:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.protocolo}', 1, 1, 'L', 1)

    pdf_content = pdf.output(dest='S').encode('latin-1')
    pdf_bytes = BytesIO(pdf_content)

    return FileResponse(pdf_bytes, as_attachment=True, filename=f"os-{servico.protocolo}.pdf")

def servico_adicional(request):
    identificador_servico = request.POST.get('identificador_servico')
    titulo = request.POST.get('titulo')
    descricao = request.POST.get('descricao')
    preco = request.POST.get('preco')

    servico_adicional = ServicoAdicional(titulo=titulo,
                                        descricao=descricao,
                                        preco=preco)

    servico_adicional.save()

    servico = Servico.objects.get(identificador=identificador_servico)
    servico.servicos_adicionais.add(servico_adicional)
    servico.save()

    return HttpResponseRedirect(reverse('servico', args=[identificador_servico]))


def apagar_servico_adicional(request, id):
    try:
        s = ServicoAdicional.objects.get(id=id)
        s.delete()
        return JsonResponse({'status': 'success', 'message': 'Serviço adicional apagado com sucesso.'})
    except ServicoAdicional.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Serviço adicional não encontrado.'}, status=404)


def realizar_servico(request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador)
    print(servico.finalizado)
    if servico.finalizado:
        servico.finalizado = False
    else:
        servico.finalizado = True
    servico.save()

    return JsonResponse({'status': 'success', 'message': 'Serviço atualizado com sucesso.'})
