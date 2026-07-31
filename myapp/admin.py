from django.contrib import admin
from .models import Staff

admin.site.register(Staff)
from .models import CrimeReport
admin.site.register(CrimeReport)