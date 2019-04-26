from rest_framework import serializers
from .models import Doctor, Patient, Rrequest, Rresponse
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)

class DoctorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    speciality = serializers.CharField(required=True)
    patient_diagnosis = serializers.CharField()
    phone_number = serializers.CharField()
    email_address = serializers.CharField()
    created_by = UserSerializer(read_only=True)


    def create(self, validated_data):
        doctor = Doctor(**validated_data)
        doctor.save()
        return doctor

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class DoctorSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    surname = serializers.CharField()
    speciality = serializers.CharField(required=True)
    patient_diagnosis = serializers.CharField()
    phone_number = serializers.CharField()
    email_address = serializers.CharField()
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Doctor
        # fields = ('id', 'name', 'created_by',)
        fields = '__all__'


class PatientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    surname = serializers.CharField()
    diagnosis = serializers.CharField()
    age = serializers.IntegerField()
    gender = serializers.CharField()
    phone_number = serializers.CharField()
    email_address = serializers.CharField()
    allergies = serializers.CharField()
    doctor = DoctorSerializer2()

    def create(self, validated_data):
        patient = Patient(**validated_data)
        patient.save()
        return patient

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class RequestSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    text = serializers.CharField()
    created_at = serializers.DateTimeField()
    doctor = DoctorSerializer2()
    patient = PatientSerializer()

    class Meta:
        model = Rrequest
        fields = '__all__'


class ResponseSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    text = serializers.CharField()
    created_at = serializers.DateTimeField()
    request = RequestSerializer2()

    class Meta:
        model = Rresponse
        fields = '__all__'

