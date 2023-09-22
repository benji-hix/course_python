from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from . import fingerspell

def index_fingerspell(request):
    return render(request, 'fingerspell.html')

def activate_fingerspell(request):
    # fingerspell.activate()
    return redirect('')