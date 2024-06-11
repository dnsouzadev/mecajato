from io import BytesIO
from django.http import FileResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from fpdf import FPDF
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
        return HttpResponseRedirect("servico/listar_servico/")
    else:
        return render(request, "servico.html", {"servico": Servico.objects.get(identificador=identificador)})


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

    pdf.cell(35, 10, 'Data de início:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.data_inicio}', 1, 1, 'L', 1)
    pdf.cell(35, 10, 'Data de entrega:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.data_entrega}', 1, 1, 'L', 1)
    pdf.cell(35, 10, 'Protocolo:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.protocolo}', 1, 1, 'L', 1)

    pdf_content = pdf.output(dest='S').encode('latin-1')
    pdf_bytes = BytesIO(pdf_content)

    return FileResponse(pdf_bytes, as_attachment=True, filename=f"os-{servico.protocolo}.pdf")
