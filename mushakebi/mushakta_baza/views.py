from django.shortcuts import render

from .models import Tan_Mshromeli
from django.http import HttpResponse
from django.core import serializers
import json

# Create your views here.

def infoo(response):

    All_Info=serializers.serialize('json',Tan_Mshromeli.objects.all())
    print('\n\n\n\n\n\n')
    

    return HttpResponse(All_Info)


def infoo2(response):

    Infoo = Tan_Mshromeli.objects.all().values()
    dic_list = []
    for i in Infoo:
        dic_list.append(i)



    Json=json.dumps( dic_list,indent=4,default=str)

    return HttpResponse(Json)
