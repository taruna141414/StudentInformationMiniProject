# from django.conf.urls import url
from mysite import views
from django.urls.conf import path
from django.contrib.auth import views as auth_views

app_name='mysite'
# app_name='mainheader'

urlpatterns = [
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('delete', views.delete_data, name='delete'),
    path('registration', views.registration, name='registration'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
]