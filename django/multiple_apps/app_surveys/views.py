from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

def show_surveys(request):
    context = {
        'message' : 'placeholder to display all of the surveys created'
    }
    return render(request, 'surveys.html', context)

def new(request):
    context = {
        'message' : 'placeholder for users to add a new survey'
    }
    return render(request, 'surveys.html', context)