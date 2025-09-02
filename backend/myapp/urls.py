from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # views.home 함수 필요
]