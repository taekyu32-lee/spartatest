from django.contrib import admin
from django.urls import path, include
from intro import views

app_name = 'intro'
urlpatterns = [
    path('introduce/', views.intro),
]
