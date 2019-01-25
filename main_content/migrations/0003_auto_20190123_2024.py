# Generated by Django 2.1.5 on 2019-01-23 20:24

from django.db import migrations, models
import main_content.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_content', '0002_project_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=main_content.models.get_image_path)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='images',
        ),
        migrations.AddField(
            model_name='projectimage',
            name='property',
            field=models.ForeignKey(on_delete=None, related_name='images', to='main_content.Project'),
        ),
    ]
