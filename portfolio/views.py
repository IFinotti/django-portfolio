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
        slug = kwargs.get('slug')

        context = {
            'principal_photo': principal_photo
        }

        if slug:
            context['project'] = project
            project = get_object_or_404(models.CodeProjects, slug=slug)
            return render(self.request, self.template_name, context)
        else: 
            context['code_projects'] = code_projects
            code_projects = models.CodeProjects.objects.all()
            return render(self.request, self.template_name, context)
    

class Art(View):
    template_name = 'portfolio/art.html'

    def get(self, request, *args, **kwargs):
        # get the value of the key 'slug', that came from the model
        slug = kwargs.get('slug')
        
        if slug:
            # if 'slug' exists, get the object ArtProjects or return a 404
            project = get_object_or_404(models.ArtProjects, slug=slug)
            # render the page, using the project as the context
            return render(self.request, self.template_name, {'project': project})
        else:
            # if "slug" doesnt exists, get all the objects 
            art_projects = models.ArtProjects.objects.all()
            # render the page, using the project list as the context
            return render(self.request, self.template_name, {'art_projects': art_projects})