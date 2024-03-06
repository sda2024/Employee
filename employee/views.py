from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Employee

def index(request):
    template = loader.get_template('index.html')
    myEmployees =Employee.objects.all().values()
    context = {
        "myEmployees": myEmployees,
    }
    return HttpResponse(template.render(context,request))