from app_colegio import views
from django.urls import path

urlpatterns = [
    path('', views.inicio, name='inicio'),
]