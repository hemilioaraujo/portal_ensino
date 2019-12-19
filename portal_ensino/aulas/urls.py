from django.urls import path
from .views import aula

urlpatterns = [
    path('aula/', aula, name='aula'),
]