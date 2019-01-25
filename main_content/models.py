import os
from django.db import models

from django.conf import settings

def get_image_path(instance, filename):
    return os.path.join('images/', filename)

class Project(models.Model):
    #the name of the project
    title = models.CharField(max_length=200)

    #the language it was written in
    language = models.CharField(max_length=50)

    #when the project was last worked on
    last_updated = models.DateField('last updated')

    #link to the github repo
    link = models.CharField(max_length=200)

    #the project's README.md
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    property = models.ForeignKey(Project, related_name='images', on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to=get_image_path)
