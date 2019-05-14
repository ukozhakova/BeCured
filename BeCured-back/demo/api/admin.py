from django.contrib import admin
from .models import Doctor, Patient, Appointment, Treatment, Profile, Receptionist


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'speciality', 'profile', )


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'homedoctor', 'profile')


@admin.register(Receptionist)
class ReceptionistAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', )


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','user_type', )
