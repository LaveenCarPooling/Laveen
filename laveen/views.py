from django import template
from django.http import HttpResponse
from django.shortcuts import render

def index(requests):
    return render(requests,'index.html')
def login(requests):
    return render(requests,'login.html')
def about(requests):
    return render(requests,'about.html')
def contactus(requests):
    return render(requests,'contactus.html')