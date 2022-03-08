from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Stud_info(models.Model):
    id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=264,unique=True,verbose_name="Student Name")
    s_address = models.CharField(max_length=200,verbose_name="Student Address")
    s_contact = models.IntegerField(blank= True,null=True,verbose_name="Contact")

    def __str__(self):
        return self.s_name

    class Meta:
        verbose_name = "Student Information"
        verbose_name_plural = "Student's Information"

class Stud_marks(models.Model):
    id = models.AutoField(primary_key=True)
    s_info = models.ForeignKey(Stud_info, on_delete=models.CASCADE)
    s_marks1 = models.IntegerField(blank=True,null=True,verbose_name="Django")
    s_marks2 = models.IntegerField(blank=True,null=True,verbose_name="Programming in R")
    s_marks3 = models.IntegerField(blank=True,null=True,verbose_name="IONIC")

    #def __str__(self):
       #return "Marks"

    def __unicode__(self):
           return u'(%s) %s' % (self.s_info)
    
    class Meta:
            verbose_name = "Student's Mark"
            verbose_name_plural = "Student's Marks"
            
class studentImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='media/')
    
def __str__(self):
    return self.image

class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    StudentName = models.CharField(max_length=200,null=True)
    StudentId  = models.CharField(max_length=50,null=True)
    LecturesAttended = models.IntegerField(null=True)
    TotalLectures  = models.IntegerField(null=True)
 
    def __str__(self):
        return self.StudentName
 
class Marks(models.Model):
    id = models.AutoField(primary_key=True)
    StudentName = models.CharField(max_length=200,null=True)
    StudentId  = models.CharField(max_length=50,null=True)
    PhysicsMarks = models.IntegerField(null=True)
    ChemistryMarks  = models.IntegerField(null=True)
    MathsMarks  = models.IntegerField(null=True)
    EnglishMarks  = models.IntegerField(null=True)
    ComputerMarks  = models.IntegerField(null=True)
 
    def __str__(self):
        return self.StudentName
 
class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    Message = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Message
