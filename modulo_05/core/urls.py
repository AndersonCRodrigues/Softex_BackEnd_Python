from django.urls import path
from .views import ListaTarefasAPIView, DetalheTarefaAPIView, MinhaView, LogoutView

app_name = 'core'
urlpatterns = [
    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    path('tarefas/<int:pk>/', DetalheTarefaAPIView.as_view(), name='detalhe-tarefa'),
    path('teste/', MinhaView.as_view(), name="teste-autenticado"),
    path('logout/', LogoutView.as_view(), name='logout'), 
]
