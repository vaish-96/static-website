from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'base.html') 

def about(request):
    return render(request,'about.html') 

def ourworks(request):
    return render(request,'ourworks.html') 

def solution(request):
    return render(request,'solution.html') 

def visionmission(request):
    return render(request,'visionmission.html') 

def service(request):
    return render(request,'ourservice.html') 