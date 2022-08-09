from django.shortcuts import render
from .models import Post

def show_blog(request):
    # context = {'posts': Post.objects.all()}
    context = {'posts': Post.objects.filter(status='pub')}#:]
    return render(request, 'blog/index.html', context)

def show_detail(request, pk):
    context = {'post': Post.objects.get(pk=pk)}
    return render(request, 'blog/post_detail.html', context)
