from django.shortcuts import render
from .models import Post

def show_blog(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/index.html', context)
