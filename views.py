
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> hi amira, Welcome to Django!</h1><p>INFRATELE Website</p>")

