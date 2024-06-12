from django.forms import ModelForm
from .models import Servico, CategoriaManutencao
from django import forms
from .widgets import CurrentDateWidget

class FormServico(ModelForm):
    class Meta:
        model = Servico
        exclude = ['finalizado', 'protocolo', 'identificador', 'servicos_adicionais']

    data_inicio = forms.DateField(label='Data de início', widget=CurrentDateWidget)
    data_entrega = forms.DateField(label='Data de entrega', widget=CurrentDateWidget)

    def __init__(self, *args, **kwargs):
        super(FormServico, self).__init__(*args, **kwargs)
        choices = list()
        for i, j in self.fields['categoria_manutencao'].choices:
            categoria = CategoriaManutencao.objects.get(titulo=j)
            choices.append((i.value, categoria.get_titulo_display())) # type: ignore

        self.fields['categoria_manutencao'].choices = choices
