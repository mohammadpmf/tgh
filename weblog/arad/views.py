from django.shortcuts import render

def show_arad(request):
    return render(request, 'arad/index.html')
