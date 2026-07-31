# myapp/urls.py
from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path('', views.login_view, name='login'),  # URL pattern for the login view
    path('home/', views.home_view, name='home'),  # URL pattern for the home view
    path('dashboard/', views.dashboard, name='dashboard'),  # URL pattern for the dashboard view
    path('crimes/', views.crime_list, name='crime_list'),  # URL pattern for the crime_list view
    path('staff/', views.staff_list, name='staff_list'),  # URL pattern for the staff_list view
]