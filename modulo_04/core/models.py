from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200) # equivale a TEXT no SQL
    concluida = models.BooleanField(default=False) # equivale a bool
    criada_em = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.titulo
