from django.forms import ModelForm
from .models import Servico, CategoriaManutencao

class FormServico(ModelForm):
    class Meta:
        model = Servico
        exclude = ['finalizado', 'protocolo']

    def __init__(self, *args, **kwargs):
        super(FormServico, self).__init__(*args, **kwargs)
        choices = list()
        for i, j in self.fields['categoria_manutencao'].choices:
            categoria = CategoriaManutencao.objects.get(titulo=j)
            choices.append((i.value, categoria.get_titulo_display())) # type: ignore

        self.fields['categoria_manutencao'].choices = choices
