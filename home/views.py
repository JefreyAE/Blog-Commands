from django.shortcuts import render, HttpResponse, redirect
from home.models import Topic

# Create your views here.

def home(request):

    title = "Home"

    # return HttpResponse(f"""    
    # """)

    topics = Topic.objects.all()
    
    
    return render(request, 'index.html', { 'topics': topics })
    


