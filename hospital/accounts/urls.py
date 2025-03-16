from django.urls import path
from .views import (
    patient_register, doctor_register, thank_you, 
    user_login, user_logout, patient_dashboard, doctor_dashboard, 
    admin_login, admin_dashboard, 
    approve_patient, approve_doctor, admin_logout,patient_list,doctor_list,
)

urlpatterns = [
    path('patient_register/', patient_register, name='patient_register'),
    path('doctor_register/', doctor_register, name='doctor_register'),
    path('thank_you/', thank_you, name='thank_you'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('admin_login/', admin_login, name='admin_login'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('approve_patient/<int:patient_id>/', approve_patient, name='approve_patient'),
    path('approve_doctor/<int:doctor_id>/', approve_doctor, name='approve_doctor'),
    path('admin_logout/', admin_logout, name='admin_logout'),
    path('patient_list/', patient_list, name='patient_list'),
#    path('patient_dashboard/', patient_list, name='patient_list'),
#    path('doctor_dashboard/', doctor_list, name='doctor_list'),
]
