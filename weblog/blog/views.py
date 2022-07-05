from django.shortcuts import render

def show_blog(request):
    return render(request, 'blog/index.html')
