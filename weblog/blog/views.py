from django.http import response
from django.shortcuts import render
from .models import Post

def show_blog(request):
    # context = {'posts': Post.objects.all()}
    context = {'posts': Post.objects.filter(status='pub')}#:]
    return render(request, 'blog/index.html', context)

def new_post(request):
    if request.method == "POST":
        # from .forms import PostForm
        # PostForm(request.POST)
        t = request.POST.get('title')
        te = request.POST.get('text')
        from django.contrib.auth.models import User
        Post.objects.create(title=t, text=te,
                            author=User.objects.first(), status='pub')

    else:
        print("Get")
    return render(request, 'blog/new_post.html')


def show_detail(request, pk):
    if request.method == "POST":
        print("OK")
    context = {'post': Post.objects.get(pk=pk)}
    return render(request, 'blog/post_detail.html', context)
