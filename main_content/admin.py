from django.contrib import admin

from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    fields = [
            'title', 
            'language', 
            'last_updated', 
            'link', 
            'description'
            ]
    inlines = [ ProjectImageInline, ]

admin.site.register(Project, ProjectAdmin)
