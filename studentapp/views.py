from django.shortcuts import render,redirect

#for import table
from adminapp.models import course1

from datetime import date

from . import models as studentmodel

#for log out
from django.contrib.auth import logout

#middleware ke liye
def sessioncheckstudent_middleware(get_response):
 def middleware(request):
    if request.path=='/studenthome/' or request.path=='/studenthome/courselist3/' or  request.path=='/studenthome/batchlist1/':
        # if request.session["emailid"]==None or request.session["role"]!="student":
        if 'emailid' not in request.session:
            response=redirect('/login/')
        else:
            response=get_response(request)
    else:
        response=get_response(request)
    return response
 return middleware 
# Create your views here.
def studenthome(request):
    #print("Welcome admin")
    #for fetch session data---------------------
    emailid=request.session.get("emailid")
    role=request.session.get("role")
    #--------------------------------------------
    return render(request,"studenthome.html",{"emailid":emailid,"role":role})

def courselist3(request):
    res= course1.objects.all()
    return render(request,"courselist3.html",{'res':res})

# def batchlist1(request):
#     s="""select a.batchid,b.name,b.duration,b.fees,
#     a.startdate,a.batchtime,a.facultyname
#       from adminapp_batch as a inner join adminapp_course1 as b on a.courseid_id=b.courseid 
#       where a.batchstatus=1;
#         """
#     res=course1.objects.raw(s)
#     return render(request,"batchlist1.html",{'res':res}) 

def batchlist1(request):
    s='''SELECT b.courseid,b.name,b.duration,b.fees,a.batchid,a.startdate,a.batchtime,a.facultyname 
       from adminapp_batch as a 
       inner join adminapp_course1 as b on a.courseid_id=b.courseid 
       where a.batchstatus=1'''
    res=course1.objects.raw(s)    #raw query ko execute pkrta hai
    return render(request,"batchlist1.html",{'res':res})

def admission(request):
    if request.method=="GET":
        batchid=request.GET.get("batchid")
        s='''SELECT b.courseid,b.name,b.duration,b.fees,a.batchid,a.startdate,a.batchtime,a.facultyname 
       from adminapp_batch as a 
       inner join adminapp_course1 as b on a.courseid_id=b.courseid 
       where a.batchid='''+batchid
        res=course1.objects.raw(s)

        return render(request,"admission.html",{'res':res})
    else:
     batchid=request.POST.get("batchid")
     emailid=request.session.get("emailid")
     #admission date
     today=date.today()
     admissiondate=today.strftime("%Y-%m-%d")
     obj=studentmodel.admission(batchid=batchid,emailid=emailid,admissiondate=admissiondate)
     obj.save()
     return render(request,"success.html",{'res':''})
    
def success(request):
    return render(request,"success.html")

def logout1(request):
    logout(request)
    return redirect('http://localhost:8000/')