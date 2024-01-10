from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import random
""""
get() : It will return object

-> It will return only single object
-> It will throw exception when it will return object
-> If conditon not match it will throw exeception
"""

# Create your views here.
def login(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(userid=uid)
        context={
                "uid":uid,
                "cid":cid,         
            }
        return render(request,"chairmanapp/index.html",context)
    else:
        return render(request,"chairmanapp/login.html")

def login_evalute(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(userid=uid)
        context={
                "uid":uid,
                "cid":cid,         
            }
        return render(request,"chairmanapp/index.html",context)
    else:
        try:
            print("=================this function is called.")
            email_var=request.POST["email"]
            password_var=request.POST["password"]
            print("=======>>>>email",email_var)
            print("------------<<<password",password_var)
            # ORM : object relational mapper
            uid=User.objects.get(email=email_var,password=password_var)
            print("---------->>> uid",uid)
            print("========<<<role",uid.role)
            print("==========is active",uid.is_active)


            if uid.role=="chairman":
                cid = Chairman.objects.get(userid=uid)
                print("Firstname =",cid.firstname)
                # Session Management
                request.session['email']=email_var

                context={
                    "uid":uid,
                    "cid":cid,         
                }
                return render(request,"chairmanapp/index.html",context)
            else:
                pass

            return render(request,"chairmanapp/login.html")
        except:
            e_msg="Invalid email or password"
            print("=====>> emsg",e_msg)
            return render(request,"chairmanapp/login.html",{"e_msg":e_msg})
def logout(request):
    if "email" in request.session:
        del request.session['email']
        return render(request,"chairmanapp/login.html")
    else:
        return render(request,"chairmanapp/login.html")
    
def chairman_profile(request): 
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(userid=uid)
        context={
                "uid":uid,
                "cid":cid,         
            }
        return render(request,"chairmanapp/profile.html",context)
    else:
        return render(request,"chairmanapp/login.html")
    
def chairman_change_password(request):
    if request.POST:
        email=request.session['email']
        currentpassword=request.POST['currentpassword']
        newpassword=request.POST['newpassword']
        uid=User.objects.get(email=email)
        if uid:
            if uid.password==currentpassword:
                uid.password=newpassword
                uid.save()      # updtae 
                del request.session['email']
                s_msg="Successfully Password Changed"
                return render(request,"chairmanapp/login.html",{'s_msg':s_msg})
            else:
                pass
        else:
            pass 

def chairman_update_profile(request):
    if request.POST:
        uid=User.objects.get(email=request.session['email'])
        cid=Chairman.objects.get(userid=uid)
        cid.firstname=request.POST['firstname']
        cid.lastname=request.POST['lastname']
        cid.contactno=request.POST['contactno']
        cid.houseno=request.POST['houseno']

        if "profilepic" in request.FILES:
            picture=request.FILES['profilepic']
            cid.pic=picture
            cid.save()
        
        cid.save()
        context={
            'uid' : uid,
            'cid' : cid,
        }
        return render(request,"chairmanapp/profile.html",context)
    
def add_member(request):
    if request.POST:
        uid=User.objects.get(email=request.session['email'])
        cid = Chairman.objects.get(userid=uid)
        context={
                "uid":uid,
                "cid":cid,         
        }
        email=request.POST['email']
        contactno=request.POST['contactno']
        l1=["x6c5","5d7sa","a6s8k","tr5u4","6bn5m","io9p8"]
        password = random.choice(l1)+email[3:6]+contactno[4:6]
        muid=User.objects.create(email=email,password=password,role='member')
        mid=Member.objects.create(userid=muid,
                                  firstname=request.POST['firstname'],
                                  lastname=request.POST['lastname'],
                                  contactno=request.POST['contactno'],
                                  houseno=request.POST['houseno'],
                                  vehicle_details=request.POST['vehicle_details'],
                                  occupation=request.POST['occupation'],
                                  no_familymembers=request.POST['no_familymembers'],
                                  job_address=request.POST['job_address'],
                                  blood_grp=request.POST['blood_grp'],
                                  city=request.POST['city'],
                                  birthdate=request.POST['birthdate'])
        print("==========================================================")
        return render(request,"chairmanapp/add_member.html",context)
    else:
        if "email" in request.session:
            uid=User.objects.get(email=request.session['email'])
            cid = Chairman.objects.get(userid=uid)
            context={
                    "uid":uid,
                    "cid":cid,         
                }
            return render(request,"chairmanapp/add_member.html",context)
        else:
            return render(request,"chairmanapp/login.html")