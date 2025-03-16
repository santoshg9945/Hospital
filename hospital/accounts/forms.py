from django import forms
from .models import Patient, Doctor
from django.contrib.auth.hashers import make_password  # To hash the password

class PatientRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = Patient
        fields = ['fullname', 'email', 'phone_number', 'date_of_birth', 'gender', 'address', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        patient = super().save(commit=False)
        patient.password = make_password(self.cleaned_data['password'])  # Hash password before saving
        if commit:
            patient.save()
        return patient


from django import forms
from django.contrib.auth.hashers import make_password
from .models import Doctor

class DoctorRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = Doctor
        fields = ['full_name', 'email', 'phone_number', 'date_of_birth', 'gender', 'specialization', 'qualification', 'experience', 'address', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        doctor = super().save(commit=False)
        doctor.password = make_password(self.cleaned_data['password'])  # Hash password before saving
        if commit:
            doctor.save()
        return doctor

    
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)  # Change to "email" if logging in with email
    password = forms.CharField(widget=forms.PasswordInput)
