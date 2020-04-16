from django.urls import path
from . import views

urlpatterns = [
    path('', views.input1, name='home-page' ),
    path('home', views.home, name='home' ),
]