from django.shortcuts import render
from django.http import HttpResponse as httpResponse
from django.template import loader
from .userModel import Users as userModel
from django.db import connection

def Users(request):
    template = loader.get_template("users.dashboard.html")
    userList = userModel.objects.all().values()

    """with connection.cursor() as cursor:
      #  cursor.execute('SELECT * FROM public."Users"')
       # global results
        results = cursor.fetchall()"""
        
 

    context = {
        "data": userList
    }
    return httpResponse(template.render(context=context, request=request))


# Create your views here.