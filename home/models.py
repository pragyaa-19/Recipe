from django.db import models

# Create your models here.

class Student(models.Model):
    #schema = databse structure -----
    #id
    name = models.CharField(max_length=10) #(string)
    age = models.IntegerField()            #(int)
    email = models.EmailField(max_length=50)   #()
    address = models.TextField(null=True, blank=True)  #()


class Car(models.Model):
    car_name = models.CharField(max_length=50)
    speed = models.IntegerField()



    #for recognizing it
    def __str__(self) -> str:
        return f"name:{self.car_name},value: {self.speed}"
    
