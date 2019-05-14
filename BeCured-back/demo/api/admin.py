from django.contrib import admin
from .models import Doctor, Patient, Appointment, Treatment, Profile, Receptionist


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('id', 'speciality', 'profile', )


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'homedoctor', 'profile')


@admin.register(Receptionist)
class ReceptionistAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile')
=======
    list_display = ('id', 'name', 'surname', 'created_by', )

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'created_by',)
>>>>>>> 6a99e93646f90f48f729fd54014df683072612ad


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('id', 'name', 'date', )
=======
    list_display = ('id', 'name', 'doctor', 'date', 'time')
>>>>>>> 6a99e93646f90f48f729fd54014df683072612ad


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('id', 'name', 'created_at', )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','user_type', )
=======
    list_display = ('id', 'name', 'created_at', 'patient')
>>>>>>> 6a99e93646f90f48f729fd54014df683072612ad
