from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.views import generic

from .models import Project

class DetailView(generic.DetailView):
    model = Project
    template_name = 'main_content/detail.html'

class HomeView(generic.DetailView):
    model = Project
    template_name='main_content/home.html'

def projects(request):
    proj_list = Project.objects.order_by('-last_updated')
    context = {'proj_list':proj_list}
    return render(request, 'main_content/index.html', context)

def about(request):
    return HttpResponse("This is about me.")

def contact(request):
    return HttpResponse("This is the contact page.")

def home(request):
    proj_list = Project.objects.order_by('-last_updated')
    context = {'proj_list':proj_list}
    return render(request, 'main_content/home.html', context)
