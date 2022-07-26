from tkinter import CASCADE
from typing_extensions import Self
from django.db import models
from datetime import datetime

# Create your models here.


class Departamenti(models.Model):
    Saxeli=models.CharField(max_length=200)
    
    Mta_Dep=models.ForeignKey('self', on_delete=models.CASCADE, blank=True,null=True)



    def __str__(self):

        if(self.Mta_Dep is not None):

            return self.Mta_Dep.__str__() + '/' + self.Saxeli

        else:

            return self.Saxeli


class Maxasiateblebi(models.Model):

    name=models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.name



class Tan_Mshromeli(models.Model):
    #პირადობაზე რაც წერია
    Saxeli = models.CharField(max_length=50)
    Gvari = models.CharField(max_length=50)
    Cit = models.CharField(max_length=50)
    Sqesi = models.CharField(max_length=1)
    Piradi_Nom = models.CharField(max_length=11)
    Dab_Tar = models.DateField(default=datetime.now())
    Vada = models.DateField(default=datetime.now())
    Surati = models.ImageField()

    Emaili = models.EmailField()
    Departamenti = models.ForeignKey(Departamenti,on_delete=models.CASCADE,null=True,blank=True)

    maxasiateblebi = models.ManyToManyField(Maxasiateblebi)

    def __str__(self):
        return self.Departamenti.__str__() + '/' + self.Saxeli






