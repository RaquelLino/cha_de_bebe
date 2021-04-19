from django.contrib import admin
from django.urls import path
from lista_presente import views
urlpatterns = [
    path('', views.lista_presentes, name="lista_presentes"),
]