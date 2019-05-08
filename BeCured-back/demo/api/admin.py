from django.contrib import admin
from .models import Doctor, Patient, Bills, Appointments, Treatments, Receptionist


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'diagnosis', )


@admin.register(Receptionist)
class ReceptionistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


@admin.register(Treatments)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Bills)
class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient')


@admin.register(Appointments)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient')

