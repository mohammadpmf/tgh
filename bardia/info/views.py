from django.shortcuts import render

def show_info(request):
    return render (request, 'info/index.html')