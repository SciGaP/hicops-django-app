
from django.urls import path

from . import views

app_name = 'hicops_django_app'
urlpatterns = [
    path('home/', views.home, name='home'),
]
