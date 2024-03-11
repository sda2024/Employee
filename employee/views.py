from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Employee
from django.urls import reverse

def index(request):
    template = loader.get_template('index.html')
    myEmployees =Employee.objects.all().values()
    context = {
        "myEmployees": myEmployees,
    }
    return HttpResponse(template.render(context,request))

def create(request):
    template = loader.get_template('createPage.html')
    return HttpResponse(template.render({},request))

def createEmployee(request):
    name = request.POST['name']
    title = request.POST['title']
    emp = Employee(name=name, title=title)
    emp.save()
    return HttpResponseRedirect(reverse("index"))

def delete(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return HttpResponseRedirect(reverse("index"))

def update(request, id):
    template = loader.get_template('updatePage.html')
    emp = Employee.objects.get(id=id)
    context = {
        "emp": emp,
    }
    return HttpResponse(template.render(context,request))

def updateEmployee(request, id):
    emp = Employee.objects.get(id=id)
    emp.name = request.POST['name']
    emp.title = request.POST['title']
    emp.save()
    return HttpResponseRedirect(reverse("index"))