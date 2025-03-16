from django.db import models

class Patient(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    address = models.TextField()
    password = models.CharField(max_length=255)  # Ensure this field exists

    is_verified = models.BooleanField(default=False)  # Admin approval field

    def __str__(self):  # Fixed the double underscores
        return self.fullname


class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    specialization = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    experience = models.IntegerField()
    address = models.TextField()
    password = models.CharField(max_length=255)  # Ensure this field exists

    is_verified = models.BooleanField(default=False)  # Admin approval field

    def __str__(self):  # Fixed the double underscores
        return self.full_name
