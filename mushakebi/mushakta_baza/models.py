from django.db import models
from datetime import datetime

# Create your models here.
class Mta_Dep(models.Model):
    Saxeli = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Saxeli


class Departamenti(models.Model):
    Saxeli=models.CharField(max_length=200)
    
    Mta_Dep=models.ForeignKey(Mta_Dep,on_delete=models.CASCADE)

    def __str__(self):
        return self.Mta_Dep.Saxeli + '/' +  self.Saxeli



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
    Departamenti = models.ForeignKey(Departamenti,on_delete=models.CASCADE)

    def __str__(self):
        return self.Departamenti.Mta_Dep.Saxeli + '/' + self.Departamenti.Saxeli + '/' + self.Saxeli

