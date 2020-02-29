from django.urls import path
from . import views

app_name ='app'

urlpatterns = [
    path('', views.base, name='base'),
    path('aboutus/', views.about, name='aboutus'),
    path('ourworks/', views.ourworks, name='ourworks'),
    path('service/', views.service, name='service'),
    path('solution/', views.solution, name='solution'),
    path('vision-and-mission/', views.visionmission, name='vision-and-mission'),
]