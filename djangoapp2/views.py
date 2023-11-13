from django.shortcuts import render,redirect
from . import models
from adminapp.models import course1

#for display img
from django.conf import settings
media_url=settings.MEDIA_URL

def home(request):
    return render(request,"master_template.html")

def register(request):
    if request.method=="GET":
        return render(request,"register.html",{'mag':''})
    else:
        fnm=request.POST.get("fnm")
        dob=request.POST.get("dob")
        gender=request.POST.get("gender")
        address=request.POST.get("address")
        city=request.POST.get("city")
        emailid=request.POST.get("emailid")
        pwd=request.POST.get("pwd")
        role="student"
        obj=models.register1(fnm=fnm,dob=dob,gender=gender,address=address,city=city,emailid=emailid,pwd=pwd,role=role)
        obj.save()
        return render(request,"register.html",{'msg':'profile created'})

def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    else:
        emailid=request.POST.get("emailid")
        pwd=request.POST.get("pwd")
        #print("login success")
        res=models.register1.objects.filter(emailid=emailid,pwd=pwd)

        if len(res)>0:
            role=res[0].role
            print("role-",role)
            #for create session------------------
            request.session["emailid"]=emailid
            request.session["role"]=role
            #------------------------------------
            if role=="admin":
                return redirect("/adminhome/")
            else:
                return redirect("/studenthome/")
        else:
            return redirect("http://localhost:8000/")
    return render(request,"login.html")


def courselist2(request):
    res=course1.objects.all()
    return render(request,"courselist2.html",{'res':res,'media_url':media_url})

