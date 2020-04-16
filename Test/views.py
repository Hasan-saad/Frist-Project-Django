from django.shortcuts import render

from django.http import HttpResponse
from .models import post

def input1(request):
    return HttpResponse('<h1>hello</h1>')

def home(request):
    grp = post.objects.all()

    context = {
        'home' : home
    }
    return render(request , 'home.html', context)