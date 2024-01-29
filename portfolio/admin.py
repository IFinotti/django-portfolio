from django.contrib import admin
from . import models
# Register your models here.

class ArtProjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_description']

admin.site.register(models.Photo)
admin.site.register(models.CodingPhoto)
admin.site.register(models.CodeProjects)
admin.site.register(models.ArtPhoto)
admin.site.register(models.ArtProjects, ArtProjectsAdmin)
