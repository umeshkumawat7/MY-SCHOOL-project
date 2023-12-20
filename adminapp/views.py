from django.shortcuts import render,redirect
from . import models as adminmodel

from django.core.files.storage import FileSystemStorage

#for display img
from django.conf import settings
media_url=settings.MEDIA_URL


from djangoapp2.models import register1


#middleware 
def sessioncheckadmin_middleware(get_response):
 def middleware(request):
    if request.path=='/adminhome/' or request.path=='/adminhome/addcourse1/' or  request.path=='/adminhome/courselist1/'  or  request.path=='/adminhome/addbatch/'  or  request.path=='/adminhome/studentlist/':
        if request.session["emailid"]==None or request.session["role"]!="admin":
            response=redirect('/login/')
        else:
            response=get_response(request)
    else:
        response=get_response(request)
    return response
 return middleware 

#for log out
from django.contrib.auth import logout
# Create your views here.

def adminhome(request):
    #print("Welcome admin")
    #for fetch session data---------------------
    emailid=request.session.get("emailid")
    role=request.session.get("role")
    #--------------------------------------------
    return render(request,"adminhome.html",{"emailid":emailid,"role":role})

def addcourse(request):
    if request.method=="GET":
        return render(request,"addcourse.html",{'msg':''})
    else:
        name=request.POST.get("name")
        duration=request.POST.get("duration")
        fees=request.POST.get("fees")
        detail=request.POST.get("detail")
        
        obj1=adminmodel.course(name=name,duration=duration,fees=fees,details=detail)
        obj1.save()
        return render(request,"addcourse.html",{'msg':'record saved'})
    
def courselist1(request):
    res=adminmodel.course1.objects.all()
    return render(request,"courselist1.html",{'res':res})

def editcourse(request):
    if request.method=="GET":
        courseid=request.GET.get("courseid")
        rs=adminmodel.course1.objects.filter(courseid=courseid)
        return render(request,"editcourse.html",{'rs':rs})
    else:
        courseid=request.POST.get("courseid")
        duration=request.POST.get("duration")
        fees=request.POST.get("fees")
        detail=request.POST.get("detail")
        adminmodel.course1.objects.filter(courseid=courseid).update(duration=duration,fees=fees,details=detail)
        return redirect("/adminhome/courselist1/")
    
def addbatch(request):
    if request.method=="GET":
        res=adminmodel.course1.objects.all()
        return render(request,"addbatch.html",{'res':res,'msg':''})
    else:
        courseid=request.POST.get("courseid")
        startdate=request.POST.get("startdate")
        batchtime=request.POST.get("batchtime")
        facultyname=request.POST.get("facultyname")
        batchstatus=1 #1 for new batch
        obj=adminmodel.batch(courseid_id=courseid,startdate=startdate,batchtime=batchtime,facultyname=facultyname,batchstatus=batchstatus)
        obj.save()
        return render(request,"addbatch.html",{'res':'','mag':'record saved'})
    

def addcourse1(request):
    if request.method=="GET":
        return render(request,"addcourse1.html",{'msg':''})
    else:
        name=request.POST.get("name")
        duration=request.POST.get("duration")
        fees=request.POST.get("fees")
        detail=request.POST.get("detail")
        #for file uploading
        courseicon=request.FILES["courseicon"]
        fs=FileSystemStorage()
        courseimg=fs.save(courseicon.name,courseicon)
        obj1=adminmodel.course1(name=name,duration=duration,fees=fees,details=detail,courseicon=courseicon)
        obj1.save()
        return render(request,"addcourse1.html",{'msg':'record saved'})
    
def studentlist(request):
    res=register1.objects.filter(role="student")
    return render(request,"studentlist.html",{'res':res})

def logout2(request):
    logout(request)
    return redirect('http://localhost:8000/')