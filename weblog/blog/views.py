from django.http import response
from django.shortcuts import render
from .models import Post

def show_blog(request):
    # context = {'posts': Post.objects.all()}
    context = {'posts': Post.objects.filter(status='pub')}#:]
    return render(request, 'blog/index.html', context)

def new_post(request):
    return render(request, 'blog/index.html')


def show_detail(request, pk):
    if request.method == "POST":
        print("OK")
    context = {'post': Post.objects.get(pk=pk)}
    return render(request, 'blog/post_detail.html', context)
