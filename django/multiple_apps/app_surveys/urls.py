from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_surveys),
    path('new', views.new),
]