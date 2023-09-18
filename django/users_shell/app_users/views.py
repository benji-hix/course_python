from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import User

def root(request):
    context = {
        'all_users' : User.objects.all()
    }
    return render(request, 'index.html', context)

def submit_user(request):
    if request.method == 'POST':
        User.objects.create(
                            first_name =request.POST['form_first_name'],
                            last_name = request.POST['form_last_name'],
                            email_address = request.POST['form_email'],
                            age = int(request.POST['form_age'])
                            )
    return redirect('/users')