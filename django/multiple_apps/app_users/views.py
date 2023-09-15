from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

# ---------------------------------------------------------------------------- #
#``                                  users views                                 #
# ---------------------------------------------------------------------------- #


def register_display(request):
    context = {
        'message' : 'placeholder for users to create a new user record'
    }
    return render(request, 'users.html', context)

def login_display(request):
    context = {
        'message' : 'placeholder for users to log in'
    }
    return render(request, 'users.html', context)

def show_users(request):
    context = {
        'message' : 'placeholder to display list of all users'
    }
    return render(request, 'users.html', context)