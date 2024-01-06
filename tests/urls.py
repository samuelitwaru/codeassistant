from django.urls import path
from .views import *

urlpatterns = [
    path('person/create', create_person, name='create_person'),
]