from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
]
