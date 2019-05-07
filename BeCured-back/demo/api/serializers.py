from rest_framework import serializers
from .models import Patient, Doctor, Receptionist, Treatment, Appointment, Bill
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class DoctorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    surname = serializers.CharField(reqired=True)
    email_address = serializers.CharField(reqired=False)
    mobile = serializers.CharField(reqired=True)
    dob = serializers.DateField(required=True)
    speciality = serializers.CharField(required=True)
    gender = serializers.CharField(reqired=True)
    qualification = serializers.CharField(reqired=True)
    created_by = UserSerializer(read_only=True)

    def create(self, validated_data):
        doctor = Doctor(**validated_data)
        doctor.save()
        return doctor

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class ReceptionistSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    surname = serializers.CharField(required=True)
    mobile = serializers.CharField(required=True)
    dob = serializers.CharField(required=True)
    gender = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Receptionist
        fields = '__all__'


class PatientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    surname = serializers.CharField(required=True)
    diagnosis = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    gender = serializers.CharField(required=True)
    mobile = serializers.CharField(required=True)
    email_address = serializers.CharField(required=False, default='absent')
    address = serializers.CharField(required=True)
    allergies = serializers.CharField(required=True)
    doctor = DoctorSerializer(read_only=True)

    def create(self, validated_data):
        patient = Patient(**validated_data)
        patient.save()
        return patient

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class TreatmentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Treatment
        fields = '_all_'


class AppointmentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Appointment
        fields = '_all_'


class BillSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Bill
        fields = '_all_'
