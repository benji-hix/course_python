from django.urls import path
from . import views
import app_navigation.views

urlpatterns = [
    path('', views.index_fingerspell),
    path('activate', views.activate_fingerspell),
    path('logout', app_navigation.views.logout)
]