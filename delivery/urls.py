from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='del-home'),
    path('about/', views.about, name='del-about'),
]