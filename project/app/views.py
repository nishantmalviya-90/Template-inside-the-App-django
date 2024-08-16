from django.shortcuts import render,redirect
from .models import Student
# Create your views here.
def register(request):
    return render(request,'h1.html')

# def home(request):
#     return redirect('https://www.instagram.com/')

def registerdata(request):
    print(request.method)
    print(request.POST)
    name=request.POST.get('name')
    email=request.POST.get('email')
    print(name,email)
    Student.objects.create(Name=name,Email=email)
    print("Data Save")