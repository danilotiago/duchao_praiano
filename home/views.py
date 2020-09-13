from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

def home(request, template_name='home/home.html'):
    data = {}
    return render(request, template_name, data)