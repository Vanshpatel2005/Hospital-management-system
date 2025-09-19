from django.contrib import admin
from .models import Patient, Doctor, Appointment

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'phone', 'created_at')
    list_filter = ('gender', 'created_at')
    search_fields = ('name', 'phone')
    ordering = ('-created_at',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'phone', 'email', 'created_at')
    list_filter = ('specialization', 'created_at')
    search_fields = ('name', 'specialization', 'email')
    ordering = ('-created_at',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'appointment_time', 'status', 'created_at')
    list_filter = ('status', 'appointment_date', 'doctor__specialization')
    search_fields = ('patient__name', 'doctor__name')
    ordering = ('-appointment_date', '-appointment_time')
    date_hierarchy = 'appointment_date'
