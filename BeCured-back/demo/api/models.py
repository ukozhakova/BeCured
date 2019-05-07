from django.db import models
from django.contrib.auth.models import User

DOCTOR_SPECIALITY = ('cardiologist', 'ophthalmologist', 'neuropathologist', 'surgeon',
                     'otorhinolaryngologist', 'endocrinologist')
USER_GENDER = ('FEMALE', 'MALE')

class DoctorManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)
    patient_diagnosis = models.CharField(max_length=200, default="")
    phone_number = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    objects = DoctorManager()
    # response = models.ForeignKey(Response, on_delete=models.CASCADE)

    def _str_(self):
        return self.name


class Receptionist(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mobile = models.CharField(null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=USER_GENDER, default='MALE')

    def _str_(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    diagnosis = models.CharField(max_length=100, choices=DIAGNOSIS, default='Z04.8-others')
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=USER_GENDER, default='MALE')
    mobile = models.CharField(max_length=20, blank=True, null=True)
    email_address = models.EmailField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100)
    allergies = models.CharField(max_length=100)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Treatment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='treat_doctor', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.patient.name

class Rrequest(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='app_doctor', on_delete=models.CASCADE)
    time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.patient.name


class Rresponse(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    request = models.ForeignKey(Rrequest, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient.name
