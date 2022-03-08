from imaplib import _Authenticator
from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from mysite.models import Stud_info,Stud_marks
from mysite.models import contact_form
from . import forms
from mysite.forms import NewStudent
from mysite.models import studentImage
from mysite.models import Attendance,Notice,Marks
from django.contrib.auth.forms import createuserform
from django.contrib.auth import login,logout,authenticate


# Create your views here.
def index(request):
     Stud_list = Stud_info.objects.order_by("s_name")
     user_data = {
          "data": Stud_list,
          }
     context_dict = {
          #'text':"and hello 'mscit' students sdsdsd",
          #'number':100,
          #'dt':datetime.now(),
          #'fruit':"cherries",
          #'link':'http://gohiltaruna.tech'
     }
     return render(request, 'index.html',context=user_data)


'''def index(request):
     # dataform = forms.FormName()
     # return render(request,"index.html",{'form':dataform})
     # return HttpResponse("HelloWorld Your First project")
     my_context = {'insert_me':''}
     return render(request,'index.html',context=my_context)'''


def about(request,id):
     
     # studentForm = NewStudent()
     # if request.method == "POST":
         # studentForm = NewStudent(request.POST)

          # if studentForm.is_valid():
               # studentForm.save(commit=True)
              # return about(request)
          # else:
               # print('Error Form Invalid')
     inst = Stud_info.objects.get(id=id)
     Stud_frm = NewStudent(request.POST or None,instance=inst)

     if Stud_frm.is_valid():
          Stud_frm.save()
     return render(request,'about.html', {'form': Stud_frm})


def registration(request):
     cform = contact_form(request.POST)
     if request.method == 'POST':
          if cform.is_valid():
               print("validation Success")
               Name = cform.cleaned_data['name']
               Email = cform.cleaned_data['email']
               print(Name," + ",Email)
            #return HttpResponseRedirect('/thanks/')
    # else:
     # form = contact_form()

     my_context = {'insert_me':''}
     return render(request,"registration.html",{'form':cform})
     # dataform = forms.FormName(request.POST)

#if dataform.is_valid():
     #print("validation Success")
    # prirnt("Student Name:"+form.cleaned_data['s_name'])
    # prirnt("Student Address:"+form.cleaned_data['s_address'])


     # return HttpResponse("HelloWorld Your First project")
    
     # return render(request,'contact.html',context=my_context)
     
def delete_data(request,id):
    if request.method == "POST":
         di = Stud_info.objects.get(id=id)
         di.delete()
         return HttpResponseRedirect('/')  
    else:
          print("Somthing is Wrong")   

def index(request):
    notice = Notice.objects.all()
    attendance = Attendance.objects.all()
    marks = Marks.objects.all()
 
    context = {
        'notice':notice,
        'marks':marks,
        'attendance':attendance,
    }
    return render(request,'index.html',context)
def addAttendance(request):    
    if request.user.is_authenticated:
        form=forms.addAttendanceform()
        if(request.method=='POST'):
            form=forms.addAttendanceform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'app/addAttendance.html',context)
    else: 
        return redirect('index')
   
def addMarks(request): 
     if request.user.is_authenticated:
        form=forms.addMarksform()
        if(request.method=='POST'):
            form=forms.addMarksform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'app/addMarks.html',context)
     else: 
        return redirect('home') 
   
   
def addNotice(request):    
    if request.user.is_authenticated:
        form=forms.addNoticeform()
        if(request.method=='POST'):
            form=forms.addNoticeform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'app/addNotice.html',context)
    else: 
        return redirect('home') 
   
   
def registerPage(request):
     if request.user.is_authenticated:
          return redirect('home') 
     else: 
        form=createuserform()
        if request.method=='POST':
            form=createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'app/register.html',context)
   
   
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=_Authenticator(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'app/login.html',context)
 
def logoutPage(request):
    LOGOUT(request)
    return redirect('/')

def studentImageView(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            photo = studentImage.objects.create(image=image,)
            photo.save()

    return render(request, 'image.html')

def setcookie(request):
      response = HttpResponse("Cookie Set")
      response.set_cookie('college', 'Geetanjali')
      return response

def getcookie(request): 
      clgname = request.COOKIES['college']
      return HttpResponse("College: "+ clgname );


def setsession(request):
     request.session['lecturer'] = 'TarunaGohil'
     request.session['email'] = 'tarunagohil@gmail.com'
     return HttpResponse("Session is Created")

def getsession(request):
     sname = request.session['lecturer']
     semail = request.session['email']
     return HttpResponse(sname +" "+ semail);