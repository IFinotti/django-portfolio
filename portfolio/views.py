from django.shortcuts import render
from . import models
from django.views import View
from django.http import HttpResponse
import os

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(self.request, 'portfolio/home.html')
    
class PrincipalPhotoView(View):
    pass