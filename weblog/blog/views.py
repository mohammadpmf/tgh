from django.http import response
from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm
from django.shortcuts import get_object_or_404

def show_blog(request):
    # context = {'posts': Post.objects.all()}
    context = {'posts': Post.objects.filter(status='pub').order_by('-date_modified')}
    return render(request, 'blog/index.html', context)

def new_post(request):
    if request.method == "POST":
        post = PostForm(request.POST)
        if post.is_valid():
            post.save()
            return redirect("blog")
    else:
        post = PostForm()
    return render(request, 'blog/new_post.html', context={'post':post})

        # t = request.POST.get('title')
        # te = request.POST.get('text')
        # from django.contrib.auth.models import User
        # Post.objects.create(title=t, text=te,
        #                     author=User.objects.first(), status='pub')

    # else:
    #     print("Get")
    # return render(request, 'blog/new_post.html')


def show_detail(request, pk):
    context = {'post': Post.objects.get(pk=pk)}
    return render(request, 'blog/post_detail.html', context)

def update_post(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    context = {'post': form }
    if form.is_valid():
        form.save()
        return redirect('blog')
    return render(request, 'blog/new_post.html', context)

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog')
