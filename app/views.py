from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        cls = request.POST.get('cls')
        
        st = Student(sname=name, spno=pno,cls=cls, email=email, username=un, pw=pw)
        st.save()
        return HttpResponse('Registration Successful')

    return render(request, 'register.html')

def users(request):
    users = Student.objects.all()
    d = {'users': users}
    return render(request, 'users.html', d)