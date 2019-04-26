from django.contrib import admin
from .models import Doctor, Patient, Rrequest, Rresponse

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'diagnosis', )


@admin.register(Rrequest)
class RrequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', )


@admin.register(Rresponse)
class RresponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', )