from django.urls import path

from . import views

app_name = 'main_content'
urlpatterns = [
    path('', views.main, name='main'),
]
