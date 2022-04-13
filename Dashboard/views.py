from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

# Create your views here.
def dashboard(request):
    return render(request,"dashboard/dashboard.html",{})

def settings(request):
    return render(request,"dashboard/settings.html",{})

def tables(request):
    return render(request,"Dashboard/tables.html",{})

