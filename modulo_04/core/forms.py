from django import forms
from .models import Tarefa # Importe o Model
# Esta classe herda de 'ModelForm'
class TarefaForm(forms.ModelForm):
# A "mágica" acontece aqui, na classe 'Meta'
    class Meta:
    # 1. Diga ao form qual Model ele deve usar
        model = Tarefa
        fields = ['titulo']