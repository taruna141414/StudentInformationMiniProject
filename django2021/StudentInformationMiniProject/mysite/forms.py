from collections import UserList
from django import forms
from django.forms.fields import CharField
from mysite.models import Stud_info
from django.forms import ModelForm
from mysite.models import Attendance,Notice,Marks
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
'''city = [
    ('rkt','Rajkot'),
    ('amd','Ahemedabad'),
    ('sur','Surat')
    ]'''
  
class contact_form(forms.Form):
    YESNO_CHOICES = (('male', 'male'), ('female', 'female'))
    sex = forms.TypedChoiceField(choices=YESNO_CHOICES, widget=forms.RadioSelect)
    name = forms.CharField(label="Full Name", required=False, max_length=100,initial="Yuor name")
    password = forms.CharField(widget=forms.PasswordInput())
    age =forms.IntegerField(label="Age",required=True)
    email = forms.EmailField(label="Email", required=False)
    birthdate = forms.DateField(label="BirthDate", required=False,widget=forms.SelectDateWidget())
    #rcity = forms.CharField(default="Rajkot",choices=city,max_length=50,verbose_name="City")
    address = forms.CharField(label="Address",required=False)
    rmb = forms.BooleanField(label="Remember Me", required=True,initial=False)
    
class NewStudent(forms.ModelForm):
    class Meta:
          model = Stud_info
          fields = '__all__'

    #class NameForm(forms.Form):
      #  s_name = forms.CharField(label='tanu', max_length=100)
       # s_address = forms.CharField(label='Rajkot', max_length=100)
class createuserform(UserCreationForm):
        class Meta:
         model=UserList
        fields=['username','password'] 
        
class addAttendanceform(forms.ModelForm):
    class Meta:
        model=Attendance
        fields="__all__"
 
class addMarksform(forms.ModelForm):
    class Meta:
        model=Marks
        fields="__all__"
 
class addNoticeform(forms.ModelForm):
    class Meta:
        model=Notice
        fields="__all__"       