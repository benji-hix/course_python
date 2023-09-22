from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from .models import User
import bcrypt

def index(request):
        return render(request, 'index.html')

def welcome(request):
    return render(request, 'welcome.html')

def account_page(request):
    return render(request, 'account.html')

def register_page(request):
    return render(request, 'register.html')

def submit_register(request):
    if request.method == 'POST':
        password = request.POST['form_password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        User.objects.create(email=request.POST['form_email'], password = pw_hash)
        request.session['logged_in'] = True
        return redirect ("/welcome")

def submit_login(request):
    user = User.objects.filter(email = request.POST['form_email'])
    if user:
        logged_user = user[0]

        if bcrypt.checkpw(request.POST['form_password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            request.session['logged_in'] = True
            return redirect ("/welcome")

def logout(request):
    request.session.clear()
    return redirect('/')