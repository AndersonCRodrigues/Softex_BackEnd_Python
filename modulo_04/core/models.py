from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

class Tarefa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tarefas')
    titulo = models.CharField(max_length=200) # equivale a TEXT no SQL
    concluida = models.BooleanField(default=False) # equivale a bool
    criada_em = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.titulo
