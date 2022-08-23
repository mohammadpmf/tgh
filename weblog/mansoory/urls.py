from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_mansoor, name='show_mansoor'),
]
