from django.shortcuts import render
from django.http import HttpResponse

def get_home(request):
    return render(request,"home/home.html")
