# recruitment_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Add other URL patterns for other views as needed
]
