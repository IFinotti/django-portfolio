# Generated by Django 4.2.7 on 2024-01-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_principalphoto_alter_projects_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(unique=True, upload_to='project_images/%Y/%m'),
        ),
    ]