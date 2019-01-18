from django.urls import path

from . import views

app_name = 'main_content'
urlpatterns = [
    path('', views.main, name='main'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
