from django.db import models
from django.contrib.auth.models import User

DOCTOR_SPECIALITY = (('cardiologist', 'cardiologist'),
                     ('ophthalmologist', 'ophthalmologist'),
                     ('neuropathologist', 'neuropathologist'),
                     ('surgeon', 'surgeon'),
                     ('otorhinolaryngologist', 'otorhinolaryngologist'),
                     ('endocrinologist', 'endocrinologist'))
USER_GENDER = (('MALE', 'MALE'), ('FEMALE', 'FEMALE'))
DIAGNOSIS = (('I10-Arterial hypertension', 'I10-Arterial hypertension'),
             ('J42-Chronical bronchitis', 'J42-Chronical bronchitis'),
             ('J06.9- cold', 'J06.9- cold'),
             ('M42-osteochondrosis', 'M42-osteochondrosis'),
             ('E10- diabetes', 'E10- diabetes'),
             ('Z04.8-others', 'Z04.8-others'))


class DoctorManager(models.Manager):
    def for_user_order_by_name(self, user):
        return self.filter(created_by=user)


class PatientManager(models.Manager):
    def for_user_order_by_name(self, user):
        return self.filter(created_by=user)


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200, choices=DOCTOR_SPECIALITY, default='endocrinologist')
    patient_diagnosis = models.CharField(max_length=200, default="")
    gender = models.CharField(max_length=10, choices=USER_GENDER, default='MALE')
    phone_number = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = DoctorManager()

    def __str__(self):
        return self.name


class Receptionist(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=200, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=USER_GENDER, default='MALE')

    def __str__(self):
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
    created_by = models.ForeignKey(User, related_name='patient_createdby', default='1', on_delete=models.CASCADE)

    objects = PatientManager()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    time = models.TimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.patient.name


class Treatment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):

        return self.patient.name


