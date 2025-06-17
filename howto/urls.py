from django.urls import path
from howto import views

urlpatterns = [
    path('', views.home, name='recipes-home')
]