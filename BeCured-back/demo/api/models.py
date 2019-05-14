from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import PermissionsMixin
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

USER_TYPE = (('Admin', 'Admin'), ('Doctor', 'Doctor'), ('Recep', 'Recep'), ('Patient', 'Patient'))

class PatientManager(models.Manager):
    def for_user_order_by_name(self, user):
        return self.filter(doctor=user)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    user_type = models.CharField(max_length=30, choices=USER_TYPE, default='Admin')
    first_name = models.CharField(max_length=100, default='', null=True)
    last_name = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=30, null=True)
    gender = models.CharField(max_length=10, choices=USER_GENDER, default='MALE')
    dob = models.DateField(blank=True, null=True, default=None)
    phone_number = models.CharField(max_length=200, default=0)

    def is_doctor(self):
        try:
            self.doctor
            return True
        except Doctor.DoesNotExist:
            return False

    def is_receptionist(self):
        try:
            self.receptionist
            return True
        except Receptionist.DoesNotExist:
            return False

    def is_patient(self):
        try:
            self.patient
            return True
        except Patient.DoesNotExist:
            return False

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.first_name


class Doctor(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    speciality = models.CharField(max_length=200, choices=DOCTOR_SPECIALITY, default='endocrinologist')

    def __str__(self):
        return self.speciality


class Receptionist(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.profile


class Patient(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    diagnosis = models.CharField(max_length=100, choices=DIAGNOSIS, default='Z04.8-others')
    address = models.CharField(max_length=100, default='')
    allergies = models.CharField(max_length=100, default='')
    homedoctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, default=1)
    objects = PatientManager()

    def __str__(self):
        return self.diagnosis


class Appointment(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=5000)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    time = models.TimeField(blank=True, null=True)
    date = models.DateField(blank=True, auto_now=True)

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


