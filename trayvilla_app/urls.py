from django.urls import path
from . import views

urlpatterns = [
    path('trayvilla_app/', views.trayvilla_app, name='trayvilla_app'),
]