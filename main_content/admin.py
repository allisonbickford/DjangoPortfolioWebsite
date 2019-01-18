from django.contrib import admin

from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Project Information',     {'fields': ['title']}),
        (None,                      {'fields': ['language']}),
        (None,                      {'fields': ['last_updated']}),
        (None,                      {'fields': ['link']}),
        (None,                      {'fields': ['description']}),
    ]

admin.site.register(Project, ProjectAdmin)
