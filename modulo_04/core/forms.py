from django import forms
from .models import Tarefa
from projects.models import Project

class TarefaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TarefaForm, self).__init__(*args, **kwargs)
  
        if user:
            self.fields['project'].queryset = Project.objects.filter(user=user)
    class Meta:
        model = Tarefa
        fields = ['titulo','project']