from django.shortcuts import render
from .models import Person

def show_info(request):
    context = {'people': Person.objects.all()}
    return render (request, 'info/index.html', context)