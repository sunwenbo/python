from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse
def index(request):
    return render(request,'myApp1/index.html')