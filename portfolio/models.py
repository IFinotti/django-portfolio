from django.db import models

# Create your models here.

class PrincipalPhoto(models.Model):
    class Meta: 
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    image = models.ImageField(upload_to='project_images/%Y/%m')
    
class Projects(models.Model):
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    name = models.CharField(max_length=25)
    short_description = models.TextField(max_length=255)
    long_description = models.TextField()
    image = models.ImageField(upload_to='project_images/%Y/%m', unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    