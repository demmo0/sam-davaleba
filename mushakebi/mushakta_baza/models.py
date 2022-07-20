from django.db import models
from datetime import datetime

# Create your models here.

class Departamenti(models.Model):
    Saxeli=models.CharField(max_length=200)

    def __str__(self):
        return self.Saxeli



class Tan_Mshromeli(models.Model):
    Saxeli = models.CharField(max_length=50)
    Gvari = models.CharField(max_length=50)
    Emaili = models.EmailField()
    Piradi_Nom = models.CharField(max_length=11)
    Dab_Tar = models.DateField(default=datetime.now())
    Departamenti = models.ForeignKey(Departamenti,on_delete=models.CASCADE)

    def __str__(self):
        return self.Saxeli

