from django.contrib import admin
from .models import *
from mysite.models import Stud_info,Stud_marks
from mysite.models import Attendance
from mysite.models import Notice,Marks
from mysite.models import Marks
# Register your models here.
admin.site.register(Stud_info)
admin.site.register(Stud_marks)
admin.site.register(Attendance)
admin.site.register(Notice)
admin.site.register(Marks)