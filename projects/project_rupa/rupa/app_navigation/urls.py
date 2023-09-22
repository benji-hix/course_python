from django.urls import path
from . import views
import app_fingerspell.views

urlpatterns = [
    path('', views.index),
    path('account', views.account_page),
    path('account/register', views.register_page),
    path('account/submit-register', views.submit_register),
    path('account/submit-login', views.submit_login),
    path('welcome', views.welcome),
    path('logout', views.logout),
]