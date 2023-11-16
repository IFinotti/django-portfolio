from django.db import models

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=25)
    short_description = models.TextField(max_length=255)
    long_description = models.TextField()
    image = models.ImageField(upload_to='project_images/%Y/%m')
    slug = models.SlugField(unique=True, blank=True, null=True)
    