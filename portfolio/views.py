from django.shortcuts import render, get_object_or_404
from . import models
from django.views import View
from django.http import HttpResponse

class Home(View):
    template_name = 'portfolio/home.html'

    def get(self, request, *args, **kwargs):
        principal_photo = models.Photo.objects.first()
        return render(request, self.template_name, {'principal_photo': principal_photo})

    
class Coding(View):
    template_name = 'portfolio/coding.html'
    
    def get(self, request, *args, **kwargs):
        principal_photo = models.CodingPhoto.objects.first()
        # get the value of the key 'slug', that came from the model
        slug = kwargs.get('slug')
        context = {'principal_photo': principal_photo}

        if slug:
            project = get_object_or_404(models.CodeProjects, slug=slug)
            context['project'] = project
            return render(self.request, self.template_name, context)
        code_projects = models.CodeProjects.objects.order_by('-id').all()
        context['code_projects'] = code_projects  
        return render(self.request, self.template_name,context)


class Art(View):
    template_name = 'portfolio/art.html'

    def get(self, request, *args, **kwargs):
        # get the value of the key 'slug', that came from the model
        slug = kwargs.get('slug')
        principal_photo = models.ArtPhoto.objects.first()
        context = {'principal_photo': principal_photo}
        
        if slug:
            project = get_object_or_404(models.ArtProjects, slug=slug)
            context['project'] = project
            return render(self.request, self.template_name, context)
        art_projects = models.ArtProjects.objects.order_by('-id').all()
        context['art_projects'] = art_projects
        return render(self.request, self.template_name, context)