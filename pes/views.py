from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello dear PES!")

# Create your views here.
