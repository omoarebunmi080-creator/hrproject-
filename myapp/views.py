from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import CrimeReport, Staff

def crime_list(request):
    crimes = CrimeReport.objects.all().order_by('-date_reported')  # Ensure date_reported exists
    return render(request, 'crime.html', {'crimes': crimes})

def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid credentials'  # Fixed the syntax error here
            }) 

    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def staff_list(request):
    staff_members = Staff.objects.all().order_by('last_name', 'first_name')  # Fixed 'staff' to 'Staff'
    return render(request, 'staff_list.html', {'staff_members': staff_members})