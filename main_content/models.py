from django.db import models

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
