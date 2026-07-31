from django.db import models


class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100, default="")
    date_joined = models.DateField()
    dob = models.DateField(null=True, blank=True)
    state_of_origin = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CrimeReport(models.Model):
    crime_type = models.CharField(max_length=100)
    location = models.CharField(max_length=255)  # Ensure this field exists
    description = models.TextField()  # Ensure this field exists
    date_reported = models.DateField(auto_now_add=True)  # Add this field


    def __str__(self):
        return self.crime_type