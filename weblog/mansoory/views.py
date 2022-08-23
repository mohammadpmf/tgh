from django.shortcuts import render

def show_mansoor(request):
    return render(request, 'mansoory/index.html')