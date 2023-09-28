from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('symptom_input/', views.symptom_input, name='symptom_input'),
    path('diagnosis/', views.diagnosis, name='diagnosis')
]