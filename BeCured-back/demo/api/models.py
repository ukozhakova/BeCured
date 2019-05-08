from django.db import models
from django.contrib.auth.models import User

DOCTOR_SPECIALITY = (('cardiologist', 'cardiologist'), ('ophthalmologist', 'ophthalmologist'),
                     ('neuropathologist', 'neuropathologist'),
                     ('surgeon', 'surgeon'), ('otorhinolaryngologist', 'otorhinolaryngologist'),
                     ('endocrinologist', 'endocrinologist'))

USER_GENDER = (('FEMALE', 'FEMALE'), ('MALE', 'MALE'))

DIAGNOSIS = (('I10', 'Arterial hypertension'), ('J42', 'Chronical bronchitis'), ('J06.9', 'cold'), ('M42', 'osteochondrosis'), ('E10',  'diabetes'))


class PatientManager(models.Manager):
    def for_user(self, user):
        return self.filter(doctor=user)


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=30, null=True)
    dob = models.DateField(blank=True, null=True)
    speciality = models.CharField(max_length=50, choices=DOCTOR_SPECIALITY)
    patient_diagnosis = models.CharField(max_length=50, choices=DIAGNOSIS)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def _str_(self):
        return self.name


class Receptionist(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=200, null=True)
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
    address = models.CharField(max_length=100, default='Tole bi 59')
    allergies = models.CharField(max_length=100)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = PatientManager

    def __str__(self):
        return self.name


class Treatments(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='treat_doctor', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.patient.name


class Bills(models.Model):
    date = models.DateField(auto_now=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatments, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.patient.name


class Appointments(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(blank=True)

    def __str__(self):
        return self.patient.name
