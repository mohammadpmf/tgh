from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_blog, name='blog'),
    path('<int:pk>', views.show_detail, name='show_detail'),
    path('new_post/', views.new_post, name='new_post'),
]