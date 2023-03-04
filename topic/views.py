from django.shortcuts import render, redirect
from home.models import *

def index(request, name='Linux', redirigir=0):

    if(redirigir == 1):
        return redirect('home', name='Paco')

    commands = Command.objects.filter(topic__name=name)
    categories = Category.objects.all()

    sideBar = "Test content"
    topics = Topic.objects.all()

    return render(request, 'topicIndex.html', {"name": name, "categories": categories, "commands": commands, "sidebar": sideBar, 'topics': topics})
