from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(self.request, 'portfolio/home.html')

