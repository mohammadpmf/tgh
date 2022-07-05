from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.say_hello, name='hello'),
]
