from django.contrib import admin
from . import models
# Register your models here.

class ArtProjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_description']

admin.site.register(models.ArtProjects, ArtProjectsAdmin)
admin.site.register(models.PrincipalPhoto)