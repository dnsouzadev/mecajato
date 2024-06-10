from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    TROCAR_VALVULA_MOTOR = 'TVM', 'Trocar válvula do motor'
    TROCAR_OLEO = 'TO', 'Trocar óleo'
    BALANCEAMENTO = 'B', 'Balanceamento',
    ALINHAMENTO = 'A', 'Alinhamento',
    REVISAO = 'R', 'Revisão',
    LAVAGEM = 'L', 'Lavagem',
    POLIMENTO = 'P', 'Polimento',
    TROCA_PNEU = 'TP', 'Troca de pneu',
    TROCA_BATERIA = 'TB', 'Troca de bateria',
    TROCA_LAMPADA = 'TL', 'Troca de lâmpada',
    TROCA_PASTILHA_FREIO = 'TPF', 'Troca de pastilha de freio',
    TROCA_DISCO_FREIO = 'TDF', 'Troca de disco de freio',

