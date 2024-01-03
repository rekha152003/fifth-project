from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

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


def insert_topic(request):
    tn=input('enter topic name')

    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)


def insert_webpage(request):
    tn=input('enter topic name')
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')
    To=Topic.objects.get(topic_name=tn)

    NWO=Webpage.objects.get_or_create(topic_name=To,name=n,url=u,email=e)[0]
    NWO.save()
    return HttpResponse('Webpage is created')

def insert_accessrecord(request):
    pk=int(input('Enter pk value of webpage'))
    a=input('enter bauthor')
    d=input('enter date')
    
    WO=Webpage.objects.get(pk=pk)

    NAO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    NAO.save()
    return HttpResponse('Access is created')
     

def update_Webpages(request):

    QLWO=Webpage.objects.all()
    d={'Webpages':QLWO}
    return render(request,'display_Webpages.html',d)

def checkbox(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        topiclist=request.POST.getlist('tn')

        QLWO=Webpage.objects.none()
        for tn in topiclist:
            QLWO=QLWO|Webpage.objects.filter(topic_name=tn)
        d1={'webpage':QLWO}
        return render(request,'display_webpages.html',d1)
    return render(request,'checkbox.html',d)


