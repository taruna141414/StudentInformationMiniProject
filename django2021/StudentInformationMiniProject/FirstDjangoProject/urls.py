"""FirstDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from os import name
from django.conf.urls import include
from django.contrib import admin
from django.urls.conf import path
from mysite.models import loginPage, logoutPage, registerPage
from mysite.forms import addAttendanceform, addMarksform, addNoticeform
from mysite import views

# from mysite.models import Stud_info,Stud_Marks

urlpatterns = [
    path('admin', admin.site.urls),
    path('index', views.index, name='index'),
    path('mysite', include('mysite.urls')),
    path('addAttendance',addAttendanceform,name='addAttendance'),
    path('addMarks',addMarksform,name='addMarks'),
    path('addNotice',addNoticeform,name='addNotice'),
    path('login', loginPage,name='login'),
    path('createuserform',name='createuserform'),
    path('logout/',logoutPage,name='logout'),
    path('register/',registerPage,name='register'),
    path('setcookie',views.setcookie,name='setcookie'),
    path('getcookie',views.getcookie,name='getcookie'),
    path('setsession',views.setsession,name='setsession'),
    path('getsession',views.getsession,name='getsession'),
]
