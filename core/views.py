from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import datetime
import json

from .models import Patient, Doctor, Appointment

def home(request):
    """Home page with dashboard statistics"""
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_appointments = Appointment.objects.count()
    today_appointments = Appointment.objects.filter(
        appointment_date=timezone.now().date()
    ).count()
    
    context = {
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'total_appointments': total_appointments,
        'today_appointments': today_appointments,
    }
    return render(request, 'core/home.html', context)

# Patient Views
def patient_list(request):
    """List all patients"""
    patients = Patient.objects.all().order_by('-created_at')
    return render(request, 'core/patient_list.html', {'patients': patients})

def patient_detail(request, pk):
    """View patient details"""
    patient = get_object_or_404(Patient, pk=pk)
    appointments = Appointment.objects.filter(patient=patient).order_by('-appointment_date')
    return render(request, 'core/patient_detail.html', {
        'patient': patient,
        'appointments': appointments
    })

def patient_create(request):
    """Create a new patient"""
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        if name and age and gender and phone:
            Patient.objects.create(
                name=name,
                age=age,
                gender=gender,
                phone=phone,
                address=address
            )
            messages.success(request, 'Patient created successfully!')
            return redirect('patient_list')
        else:
            messages.error(request, 'Please fill all required fields.')
    
    return render(request, 'core/patient_form.html')

def patient_update(request, pk):
    """Update patient information"""
    patient = get_object_or_404(Patient, pk=pk)
    
    if request.method == 'POST':
        patient.name = request.POST.get('name')
        patient.age = request.POST.get('age')
        patient.gender = request.POST.get('gender')
        patient.phone = request.POST.get('phone')
        patient.address = request.POST.get('address')
        patient.save()
        
        messages.success(request, 'Patient updated successfully!')
        return redirect('patient_detail', pk=pk)
    
    return render(request, 'core/patient_form.html', {'patient': patient})

def patient_delete(request, pk):
    """Delete a patient"""
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Patient deleted successfully!')
        return redirect('patient_list')
    return render(request, 'core/patient_confirm_delete.html', {'patient': patient})

# Doctor Views
def doctor_list(request):
    """List all doctors"""
    doctors = Doctor.objects.all().order_by('-created_at')
    return render(request, 'core/doctor_list.html', {'doctors': doctors})

def doctor_detail(request, pk):
    """View doctor details"""
    doctor = get_object_or_404(Doctor, pk=pk)
    appointments = Appointment.objects.filter(doctor=doctor).order_by('-appointment_date')
    return render(request, 'core/doctor_detail.html', {
        'doctor': doctor,
        'appointments': appointments
    })

def doctor_create(request):
    """Create a new doctor"""
    if request.method == 'POST':
        name = request.POST.get('name')
        specialization = request.POST.get('specialization')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        
        if name and specialization and phone and email:
            Doctor.objects.create(
                name=name,
                specialization=specialization,
                phone=phone,
                email=email
            )
            messages.success(request, 'Doctor created successfully!')
            return redirect('doctor_list')
        else:
            messages.error(request, 'Please fill all required fields.')
    
    return render(request, 'core/doctor_form.html')

def doctor_update(request, pk):
    """Update doctor information"""
    doctor = get_object_or_404(Doctor, pk=pk)
    
    if request.method == 'POST':
        doctor.name = request.POST.get('name')
        doctor.specialization = request.POST.get('specialization')
        doctor.phone = request.POST.get('phone')
        doctor.email = request.POST.get('email')
        doctor.save()
        
        messages.success(request, 'Doctor updated successfully!')
        return redirect('doctor_detail', pk=pk)
    
    return render(request, 'core/doctor_form.html', {'doctor': doctor})

def doctor_delete(request, pk):
    """Delete a doctor"""
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        messages.success(request, 'Doctor deleted successfully!')
        return redirect('doctor_list')
    return render(request, 'core/doctor_confirm_delete.html', {'doctor': doctor})

# Appointment Views
def appointment_list(request):
    """List all appointments"""
    appointments = Appointment.objects.all().order_by('-appointment_date', '-appointment_time')
    return render(request, 'core/appointment_list.html', {'appointments': appointments})

def appointment_detail(request, pk):
    """View appointment details"""
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'core/appointment_detail.html', {'appointment': appointment})

def appointment_create(request):
    """Create a new appointment"""
    if request.method == 'POST':
        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        notes = request.POST.get('notes')
        
        if patient_id and doctor_id and appointment_date and appointment_time:
            patient = get_object_or_404(Patient, pk=patient_id)
            doctor = get_object_or_404(Doctor, pk=doctor_id)
            
            Appointment.objects.create(
                patient=patient,
                doctor=doctor,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
                notes=notes
            )
            messages.success(request, 'Appointment created successfully!')
            return redirect('appointment_list')
        else:
            messages.error(request, 'Please fill all required fields.')
    
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'core/appointment_form.html', {
        'patients': patients,
        'doctors': doctors
    })

def appointment_update(request, pk):
    """Update appointment information"""
    appointment = get_object_or_404(Appointment, pk=pk)
    
    if request.method == 'POST':
        appointment.patient_id = request.POST.get('patient')
        appointment.doctor_id = request.POST.get('doctor')
        appointment.appointment_date = request.POST.get('appointment_date')
        appointment.appointment_time = request.POST.get('appointment_time')
        appointment.status = request.POST.get('status')
        appointment.notes = request.POST.get('notes')
        appointment.save()
        
        messages.success(request, 'Appointment updated successfully!')
        return redirect('appointment_detail', pk=pk)
    
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'core/appointment_form.html', {
        'appointment': appointment,
        'patients': patients,
        'doctors': doctors
    })

def appointment_delete(request, pk):
    """Delete an appointment"""
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Appointment deleted successfully!')
        return redirect('appointment_list')
    return render(request, 'core/appointment_confirm_delete.html', {'appointment': appointment})
