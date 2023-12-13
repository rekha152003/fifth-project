from django.shortcuts import render
from app.models import *

def display_topics(request):

    QLTO=Topic.objects.all()

    d={'topics':QLTO}

    return render(request,'display_topics.html',d)

def display_Webpages(request):

    QLTO=Webpage.objects.all()

    d={'webpages':QLTO}

    return render(request,'display_Webpages.html',d)

def display_Accessrecords(request):

    QLTO=AccessRecord.objects.all()

    d={'accessrecords':QLTO}
    
    return render(request,'display_accessrecords.html',d)

# Create your views here
