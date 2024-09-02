from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Receipe(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    Receipe_name = models.CharField(max_length=100)
    Receipe_dics= models.TextField()
    Receipe_image= models.ImageField(upload_to="receipe")
    Receipe_view_count = models.IntegerField(default=1)




class Department(models.Model):

    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    

    #sequence 
    class Meta:
        ordering=['department']

class StudentID(models.Model):
    student_id = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.student_id
    

class Student(models.Model):
    department=models.ForeignKey(Department, related_name="depart",on_delete=models.CASCADE) #one to many feild
    student_id = models.OneToOneField(StudentID,related_name="studentid", on_delete=models.CASCADE) ##one to one feild
    student_name= models.CharField(max_length=100)
    student_age= models.IntegerField(default=18)
    student_email= models.EmailField(unique=True) #true-
    student_address = models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "student"
    
