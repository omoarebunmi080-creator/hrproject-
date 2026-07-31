from django.contrib import admin
from django.urls import path, include  # Include the include function

# Customizing the admin site headers
admin.site.site_header = "Koladaisi University Admin"
admin.site.site_title = "Koladaisi University Portal"  # Fixed typo in 'site_title'
admin.site.index_title = "Welcome to Koladaisi Management System"  # Capitalized 'System'

urlpatterns = [
    path('admin/', admin.site.urls),  # URL pattern for the admin site
    path('', include('myapp.urls')),  # Include the URLs from myapp
]