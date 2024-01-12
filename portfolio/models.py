from django.conf import settings
from django.db import models
from PIL import Image
import os


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


    @staticmethod  # <- there is no 'self' in the method
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(img_full_path, optimize=True, quality=100)
    