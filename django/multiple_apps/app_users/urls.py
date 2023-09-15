from django.urls import path
from . import views
import app_blogs.views

# ---------------------------------------------------------------------------- #
#``                                  users urls                                  #
# ---------------------------------------------------------------------------- #

urlpatterns = [
    path('register', views.register_display),
    path('login', views.login_display),
    path('users/new', views.register_display),
    path('users', views.show_users),
    path('', app_blogs.views.index)
]