from django.shortcuts import render

# Create your views here.
from app.models import *

def display_topics(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'display_topics.html',d)

def dispaly_webpage(request):
    QSW=Webpage.objects.all()
    d={'webpage':QSW}
    return render(request,'display_webpage.html',d)



def display_Access(request):
    QSA=Access_Records.objects.all()
    d={'Access':QSA}
    return render(request,'display_Access.html',d)