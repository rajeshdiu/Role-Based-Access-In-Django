from django.shortcuts import render, redirect
from django.http import HttpResponse
from myApp.models import * 


def photoPage(req):
    
    photo_data=imageGallerymodel.objects.all()
    
    context={
        'data':photo_data
    }
    
    
    return render(req,'photo.html',context)


def contactPage(req):
    
    
    return render(req,'contact.html')