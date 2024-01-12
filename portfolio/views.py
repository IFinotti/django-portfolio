from django.shortcuts import render
from . import models
from django.views import View
from django.http import HttpResponse
import os

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(self.request, 'portfolio/home.html')
    
class PrincipalPhotoView(View):
    template_name = 'portfolio/principal_photo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtendo a instância mais recente de PrincipalPhoto
        principal_photo = models.PrincipalPhoto.objects.latest() 

        context['principal_photo'] = principal_photo
        return context