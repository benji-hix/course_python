from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def account_page(request):
    return render(request, 'account.html')