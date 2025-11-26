from django.contrib import admin
from .models import Tarefa

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'user', 'get_user_email','concluida', 'criada_em', 'project')
    list_filter = ('concluida', 'user', 'criada_em', 'project')
    search_fields = ('titulo', 'user__username', 'project')

    fieldsets = (
        ('Informações Principais', {
        'fields': ('user', 'titulo')
        }),
        ('Status da Tarefa', {
        'fields': ('concluida', 'criada_em')
        }),
        )

    readonly_fields = ('criada_em',)

    @admin.display(description='Email do Usuário') 
    def get_user_email(self, obj):
        return obj.user.email


admin.site.register(Tarefa, TarefaAdmin)