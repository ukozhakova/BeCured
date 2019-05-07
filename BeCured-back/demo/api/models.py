from django.db import models
from django.contrib.auth.models import User

DOCTOR_SPECIALITY = ('cardiologist', 'ophthalmologist', 'neuropathologist', 'surgeon',
                     'otorhinolaryngologist', 'endocrinologist')
USER_GENDER = ('FEMALE', 'MALE')

DIAGNOSIS = ('I10-arterial hypertension', 'Z04.8-others', 'J42-chronical bronchitis', 'J06.9-ARVI',
             'J44.0-COPD', 'E11-diabetes')


class PatientManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True)
    mobile = models.CharField(null=True)
    dob = models.DateField(blank=True, null=True)
    speciality = models.CharField(max_length=20, choices=DOCTOR_SPECIALITY, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=USER_GENDER, default='MALE')
    qualification = models.CharField(max_length=300, blank=True, null=True)

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


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='app_doctor', on_delete=models.CASCADE)
    time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.patient.name


class Bill(models.Model):
    date = models.DateField(auto_now=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='bill_doctor', on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.patient.name
