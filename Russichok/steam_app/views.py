from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def community_login(request):
    return render(request, "community_login.html")
    