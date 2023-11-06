from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Student


def home(request):
    data = Student.objects.all()
    # context = {"data":data}
    return render(request, 'index.html', {"data": data})


def insertData(request):
    if request.method == 'POST':
        name = request.POST.get("")
        email = request.POST.get("")
        age = request.POST.get("")
        gender = request.POST.get("")
        query = Student(name=name, email=email, age=age, gender=gender)
        query.save()
        return redirect('/')
    return render(request, 'index.html')


def updateData(request, id):
    if request.method == 'POST':
        name = request.POST.get("")
        email = request.POST.get("")
        age = request.POST.get("")
        gender = request.POST.get("")

        edit = Student.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.age = age
        edit.gender = gender
        edit.save()
        return redirect('/')
    else:
        d = Student.objects.get(id=id)
        return render(request, 'index.html', {'d': d})

def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect('/')
    return render(request, 'index.html')
