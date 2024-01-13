from django.shortcuts import render, get_object_or_404
from . import models
from django.views import View
from django.http import HttpResponse
import os

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(self.request, 'portfolio/home.html')
    
class Coding(View):
    def get(self, request, *args, **kwargs):
        return render(self.request, 'portfolio/coding.html')
    
class Art(View):
    template_name = 'portfolio/art.html'

    def get(self, request, *args, **kwargs):
        # Verifica se há um slug na URL
        slug = kwargs.get('slug')
        
        if slug:
            # Se houver um slug, exibe os detalhes do projeto específico
            project = get_object_or_404(models.ArtProjects, slug=slug)
            return render(self.request, self.template_name, {'project': project})
        else:
            # Se não houver slug, exibe a lista de projetos
            art_projects = models.ArtProjects.objects.all()
            return render(self.request, self.template_name, {'art_projects': art_projects})