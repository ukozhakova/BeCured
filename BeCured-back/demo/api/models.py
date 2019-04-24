from django.db import models
from django.contrib.auth.models import User


class PatientManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)
    patient_diagnosis = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    # response = models.ForeignKey(Response, on_delete=models.CASCADE)


    def __str__(self):
        return '{}, {}, {}'.format(self.surname, self.name, self.speciality)

class Patient(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    diagnosis = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    allergies = models.CharField(max_length=200)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}'.format(self.surname, self.name, self.diagnosis)

class Rrequest(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.name, self.created_at)

class Rresponse(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    request = models.ForeignKey(Rrequest, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.name, self.created_at)