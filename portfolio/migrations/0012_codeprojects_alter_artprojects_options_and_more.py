# Generated by Django 4.2.7 on 2024-01-28 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_codingphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('short_description', models.TextField(max_length=255)),
                ('long_description', models.TextField()),
                ('image', models.ImageField(unique=True, upload_to='code_images/%Y/%m')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Code project',
                'verbose_name_plural': 'Code projects',
            },
        ),
        migrations.AlterModelOptions(
            name='artprojects',
            options={'verbose_name': 'Draw', 'verbose_name_plural': 'Draws'},
        ),
        migrations.AlterModelOptions(
            name='codingphoto',
            options={'verbose_name': 'Code photo'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Home photo'},
        ),
    ]
