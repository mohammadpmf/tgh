from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_blog, name='show_blog'),
    path('<int:pk>', views.show_detail, name='show_detail'),
]