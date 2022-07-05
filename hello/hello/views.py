from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    context = {
        'username': 'mohammadpmf',
        'nat_code': '0012751452',
        'menu': ['kebab', 'koobideh', 'joojeh', 'fesenjoon'],
        'grades': [1,2,3,4,3],
    }   
    return render(request, 'hello/home.html', context)