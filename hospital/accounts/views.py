from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from .forms import PatientRegistrationForm, DoctorRegistrationForm
from .models import Patient, Doctor
from .forms import LoginForm  # Ensure this form exists
from django.http import JsonResponse



User = get_user_model()  # Get Django's user model

# ✅ ADMIN DASHBOARD (Only Pending Patients & Doctors)
# ✅ ADMIN DASHBOARD (Now shows only pending users)
@login_required
def admin_dashboard(request):
    total_patients = Patient.objects.count()
    pending_patients = Patient.objects.filter(is_verified=False).count()
    approved_patients = Patient.objects.filter(is_verified=True).count()

    total_doctors = Doctor.objects.count()
    pending_doctors = Doctor.objects.filter(is_verified=False).count()
    approved_doctors = Doctor.objects.filter(is_verified=True).count()

    # Fetch only pending patients and doctors
    pending_patient_list = Patient.objects.filter(is_verified=False)
    pending_doctor_list = Doctor.objects.filter(is_verified=False)

    context = {
        'total_patients': total_patients,
        'pending_patients': pending_patients,
        'approved_patients': approved_patients,
        'total_doctors': total_doctors,
        'pending_doctors': pending_doctors,
        'approved_doctors': approved_doctors,
        'pending_patient_list': pending_patient_list,
        'pending_doctor_list': pending_doctor_list
    }

    return render(request, 'accounts/admin_dashboard.html', context)

# ✅ PATIENT DASHBOARD (Only Approved Patients)
# ✅ PATIENT DASHBOARD
# @login_required
def patient_dashboard(request):
    patients = Patient.objects.filter(is_verified=True)
    return render(request, 'accounts/patient_list.html', {'patients': patients})
    # if request.session.get('user_type') == "patient":
    #     patient = get_object_or_404(Patient, email=request.session['user_email'])

    #     # ❌ If the patient is not approved, show pending page
    #     if not patient.is_verified:
    #         return render(request, 'accounts/pending_approval.html')

    #     return render(request, 'accounts/patient_dashboard.html', {'patient': patient})

    # return redirect('login')

# ✅ DOCTOR DASHBOARD
# @login_required
def doctor_dashboard(request):
    doctors = Doctor.objects.filter(is_verified=True)
    return render(request, 'accounts/doctor_list.html', {'doctors': doctors})
    # if request.session.get('user_type') == "doctor":
    #     doctor = get_object_or_404(Doctor, email=request.session['user_email'])

    #     # ❌ If the doctor is not approved, show pending page
    #     if not doctor.is_verified:
    #         return render(request, 'accounts/pending_approval.html')

    #     return render(request, 'accounts/doctor_dashboard.html', {'doctor': doctor})

    # return redirect('login')



# ✅ PATIENT LIST (Only Approved Patients)
@login_required
def patient_list(request):
    patients = Patient.objects.filter(is_verified=True)
    return render(request, 'accounts/patient_list.html', {'patients': patients})

# ✅ DOCTOR LIST (Only Approved Doctors)
@login_required
def doctor_list(request):
    doctors = Doctor.objects.filter(is_verified=True)
    return render(request, 'accounts/doctor_list.html', {'doctors': doctors})

# def user_login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data["email"]
#             password = form.cleaned_data["password"]
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect("dashboard")  # Redirect to the dashboard
#             else:
#                 messages.error(request, "Invalid credentials")
#     else:
#         form = LoginForm()
#     return render(request, "accounts/login.html", {"form": form})




# altered after abeove
# from django.contrib.auth import get_user_model

# User = get_user_model()  # Django's User model for admin authentication

# def user_login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # ✅ Check if the user is an Admin (Superuser)
#         admin_user = User.objects.filter(email=email, is_superuser=True).first()

#         if admin_user and admin_user.check_password(password):
#             login(request, admin_user)  # Django login function for admin
#             request.session['user_type'] = 'admin'
#             request.session['user_id'] = admin_user.id
#             messages.success(request, "Admin Login Successful!")
#             return redirect('admin_dashboard')  # Redirect to Admin Dashboard

#         # ✅ Check if the user is a Doctor
#         doctor = Doctor.objects.filter(email=email).first()
#         patient = Patient.objects.filter(email=email).first()

#         if doctor and check_password(password, doctor.password):
#             request.session['user_type'] = 'doctor'
#             request.session['user_id'] = doctor.id
#             messages.success(request, "Doctor Login Successful!")
#             return redirect('doctor_dashboard')  # Redirect to Doctor Dashboard

#         elif patient and check_password(password, patient.password):
#             request.session['user_type'] = 'patient'
#             request.session['user_id'] = patient.id
#             messages.success(request, "Patient Login Successful!")
#             return redirect('patient_dashboard')  # Redirect to Patient Dashboard

#         else:
#             messages.error(request, "Invalid Email or Password")
#             return redirect('login')

#     return render(request, 'accounts/login.html')



# working but no mesage onnnnnn
# from django.contrib.auth import get_user_model

# User = get_user_model()  # Django's User model for admin authentication

# def user_login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # ✅ Admin Login
#         admin_user = User.objects.filter(email=email, is_superuser=True).first()
#         if admin_user and admin_user.check_password(password):
#             login(request, admin_user)  # Django login for admin
#             request.session['user_type'] = 'admin'
#             request.session['user_id'] = admin_user.id
#             messages.success(request, "Admin Login Successful!")
#             return redirect('admin_dashboard')  

#         # ✅ Doctor Login
#         doctor = Doctor.objects.filter(email=email).first()
#         if doctor and check_password(password, doctor.password):
#             if not doctor.is_verified:  # ❌ If not approved
#                 messages.warning(request, "Your account is still under approval process.")
#                 return redirect('login')

#             request.session['user_type'] = 'doctor'
#             request.session['user_id'] = doctor.id
#             messages.success(request, "Doctor Login Successful!")
#             return redirect('doctor_dashboard')

#         # ✅ Patient Login
#         patient = Patient.objects.filter(email=email).first()
#         if patient and check_password(password, patient.password):
#             if not patient.is_verified:  # ❌ If not approved
#                 messages.warning(request, "Your account is still under approval process.")
#                 return redirect('login')

#             request.session['user_type'] = 'patient'
#             request.session['user_id'] = patient.id
#             messages.success(request, "Patient Login Successful!")
#             return redirect('patient_dashboard')

#         # ❌ Invalid Credentials
#         messages.error(request, "Invalid Email or Password")
#         return redirect('login')

#     return render(request, 'accounts/login.html')


from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Fetch user (Doctor or Patient)
        doctor = Doctor.objects.filter(email=email).first()
        patient = Patient.objects.filter(email=email).first()

        if doctor:
            if not doctor.is_verified:  # ❌ Not approved
                messages.warning(request, "Your account is still under approval process.")
                return redirect('login')
            if check_password(password, doctor.password):  # ✅ Correct password
                request.session['user_type'] = 'doctor'
                request.session['user_id'] = doctor.id
                messages.success(request, "Login Successful!")
                return redirect('doctor_dashboard')
            else:
                messages.error(request, "Invalid email or password.")
                return redirect('login')

        elif patient:
            if not patient.is_verified:  # ❌ Not approved
                messages.warning(request, "Your account is still under approval process.")
                return redirect('login')
            if check_password(password, patient.password):  # ✅ Correct password
                request.session['user_type'] = 'patient'
                request.session['user_id'] = patient.id
                messages.success(request, "Login Successful!")
                return redirect('patient_dashboard')
            else:
                messages.error(request, "Invalid email or password.")
                return redirect('login')

        # ❌ Email not registered
        messages.error(request, "Invalid email or still under approval process.")
        return redirect('login')

    return render(request, 'accounts/login.html')




from django.shortcuts import render

def patient_register(request):
    return render(request, 'accounts/patient_register.html')
from django.shortcuts import render

def doctor_register(request):
    return render(request, 'accounts/doctor_register.html')

def thank_you(request):
    return render(request, 'accounts/thank_you.html')

def user_logout(request):
    logout(request)
    return redirect('login')  # or any page you want to redirect after logout

def admin_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.filter(email=email).first()  # Get first matching user
            if user and user.is_superuser:  # Ensure the user is an admin
                auth_user = authenticate(request, username=user.username, password=password)
                if auth_user is not None:
                    login(request, auth_user)
                    return redirect("admin_dashboard")  # Redirect to dashboard
                else:
                    messages.error(request, "Incorrect password.")
            else:
                messages.error(request, "Not an admin account.")
        except User.DoesNotExist:
            messages.error(request, "Admin user does not exist.")

    return render(request, "accounts/admin_login.html")

from django.shortcuts import render, redirect
from .forms import PatientRegistrationForm, DoctorRegistrationForm

def patient_register(request):
    if request.method == "POST":
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect to a thank you page
    else:
        form = PatientRegistrationForm()

    return render(request, 'accounts/patient_register.html', {'form': form})

def doctor_register(request):
    if request.method == "POST":
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = DoctorRegistrationForm()

    return render(request, 'accounts/doctor_register.html', {'form': form})


from django.shortcuts import get_object_or_404, redirect
from .models import Patient

def approve_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    patient.is_verified = True
    patient.save()
    return redirect('admin_dashboard')

def approve_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    doctor.is_verified = True
    doctor.save()
    return redirect('admin_dashboard')

def admin_logout(request):
    logout(request)  # Logs out the admin
    return redirect('admin_login')  # Redirect to admin login page
