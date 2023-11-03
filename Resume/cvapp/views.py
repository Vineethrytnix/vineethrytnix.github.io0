from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.db.models import Q
# from django.contrib.auth import authenticate, logout, login
# from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
import datetime as dt
from django.core.files.storage import default_storage

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    view=Skill_percentage.objects.all()
    exp=Experience.objects.all()
    education=Education.objects.all()
    return render(request,"about.html",{"view":view,"exp":exp,"education":education})

def portfolio(request):
    view=Experience.objects.all()
    return render(request,"portfolio.html",{"view":view})

def contact(request):
    return render(request,"contact.html")