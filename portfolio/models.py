from django.db import models
from PIL import Image
from django.utils.text import slugify
from django.conf import settings
import os



# Create your models here.
class MainPhoto(models.Model):
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    image = models.ImageField(upload_to='main_photo/%Y/%m', unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)



class ArtProjects(models.Model):
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    name = models.CharField(max_length=25)
    short_description = models.TextField(max_length=255)
    long_description = models.TextField()
    image = models.ImageField(upload_to='project_images/%Y/%m', unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    @staticmethod  # <- there is no 'self' in the method
    def resize_image(img, new_size=(1080, 1080)):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if (original_width, original_height) <= new_size:
            img_pil.close()
            return

        new_img = img_pil.resize(new_size, Image.LANCZOS)
        new_img.save(img_full_path, optimize=True, quality=50)


    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.name)}-{self.pk}'
            self.slug = slug

        super().save(*args, **kwargs)

        target_size = (1080, 1080)

        if self.image:
            self.resize_image(self.image, target_size)

    def __str__(self):
        return self.name


    
    