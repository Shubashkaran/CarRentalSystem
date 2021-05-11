from django.shortcuts import render,redirect
from django.http import *
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Forming

# Create your views here.
def index(request):
    proj=Recent.objects.all()
    abouti=about.objects.all()
    slide=slideshow.objects.all()
    return render(request, "index.html", {'tem': proj, 'abou':abouti, 'slide':slide})

def booking(request):
    book = Booking.objects.all()
    return render(request, "Booking.html", {'ook': book})

def camp(request):
    uname = request.POST.get("uname")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    pdate = request.POST.get("pdate")
    ddate = request.POST.get("ddate")
    passa = int(request.POST.get("passa"))
    result = int(request.POST.get("result"))
    book_info = Forming(uname=uname,email=email,phone=phone,pdate=pdate,ddate=ddate,passa=passa,result=result)
    book_info.save()
    return redirect('redirect1')

def Success(request):
    return render(request,"Success.html")

def redirect1(request):
    return HttpResponseRedirect('Success')

