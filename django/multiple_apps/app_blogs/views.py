from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

def index(request):
    context = {
        'message' : 'placeholder to display a list of all blogs',
    }
    return render(request, 'blogs.html', context)


def new(request):
    context = {
        'message' : 'placeholder to a new form to create new blog'
    }
    return render(request, 'blogs.html', context)

    
def create(request):
    return redirect('/blogs')


def show(request, number):
    context = {
        'message' : f'placeholder to edit blog {number}'
    }
    return render(request, 'blogs.html', context)


def edit(request, number):
    context = {
        'message' : f'placeholder to edit blog {number}'
    }
    return render(request, 'blogs.html', context)


def destroy(request, number):

    return redirect('/blogs')

