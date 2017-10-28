from django.contrib import admin
from .models import Projects


# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'start_date', 'end_date')
    search_fields = ('project_name',)
    list_filter = ('start_date', 'end_date')

admin.site.register(Projects, ProjectsAdmin)
