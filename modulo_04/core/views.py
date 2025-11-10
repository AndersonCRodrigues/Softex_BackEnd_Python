from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarefa

# Create your views here.
def home(request):
    todas_as_tarefas = Tarefa.objects.all()

    context = {
        'nome_usuario': 'Júnior',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS'],
        'tarefas': todas_as_tarefas,
    }
    # return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")
    return render(request, 'home.html', context)

def login(request):
    return HttpResponse("<input>Login</input>")