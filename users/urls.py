from django.contrib import admin
from django.urls import path
from . import views as userViews

urlpatterns = [
    path('', userViews.Users, name="user dashboard")
]