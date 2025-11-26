from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'user')
    search_fields = ('titulo', 'user__username')
    list_filter = ('user',)

admin.site.register(Project, ProjectAdmin)