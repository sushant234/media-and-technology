from django.shortcuts import render
from app.models import *
# Create your views here.


def home(request):
    context={}
    context['employee'] = employee.objects.all()
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

def servicess(request):
    context={}
    context['services'] = services.objects.all()
    return render(request,'services.html',context)

def blogs(request):
    context={}
    context['blog'] = blogg.objects.all()
    return render(request,'blog.html',context)

def single_blogs(request,value):
    context={}
    context['sblog'] = blogg.objects.get(id=value)
    return render(request,'blog-single.html',context)