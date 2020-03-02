from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'base.html') 

def about(request):
    return render(request,'about.html',{'title':'About us'}) 

def ourworks(request):
    return render(request,'ourworks.html',{'title':'Our Work'}) 

def solution(request):
    return render(request,'solution.html',{'title':'Solution'}) 

def visionmission(request):
    return render(request,'visionmission.html',{'title':'Mission and Vission'}) 

def service(request):
    return render(request,'ourservice.html',{'title':'Our service'}) 