from django.contrib import admin
from .models import Patient, Doctor  

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phone_number', 'date_of_birth', 'gender','address')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number','date_of_birth','gender','specialization', 'qualification','experience','address')



