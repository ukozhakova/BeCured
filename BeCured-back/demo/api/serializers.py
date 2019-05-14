from rest_framework import serializers
<<<<<<< HEAD
from .models import Doctor, Patient, Appointment, Treatment, Receptionist, Profile
=======
from .models import Doctor, Patient, Appointment, Treatment
from .models import Doctor, Patient, Appointment, Treatment, Receptionist
>>>>>>> 6a99e93646f90f48f729fd54014df683072612ad
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    user_type = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    gender = serializers.CharField(required=True)
    dob = serializers.DateField(required=True)
    phone_number = serializers.CharField(required=True)

    class Meta:
        model = Profile
        fields = '__all__'


class DoctorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    profile = ProfileSerializer()
    speciality = serializers.CharField(required=True)

    def create(self, validated_data):
        doctor = Doctor(**validated_data)
        doctor.save()
        return doctor

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.speciality = validated_data.get('speciality', instance.speciality)
        instance.patient_diagnosis = validated_data.get('patient_diagnosis', instance.patient_diagnosis)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email_address = validated_data.get('email_address', instance.email_address)

        instance.save()
        return instance

    class Meta:
        model = Doctor
        fields = ('id', 'name', 'surname',)


class ReceptionistSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Receptionist
        fields = ('id', 'name', 'surname',)


class PatientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    diagnosis = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    allergies = serializers.CharField(required=True)
    homedoctor = DoctorSerializer(read_only=True)

    def create(self, validated_data):
        patient = Patient(**validated_data)
        patient.save()
        return patient

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.diagnosis = validated_data.get('diagnosis', instance.diagnosis)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.email_address = validated_data.get('email_address', instance.email_address)
        instance.address = validated_data.get('address', instance.address)
        instance.allergies = validated_data.get('allergies', instance.allergies)
        instance.save()
        return instance

    class Meta:
        model = Patient
        fields = ('id', 'name', 'surname',)

#Serializer2
class DoctorSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = Doctor
        fields = ('id', 'name', 'surname')


class PatientSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)


    class Meta:
        model = Patient
        fields = ('id', 'name', 'surname', 'diagnosis', 'mobile')


class TreatmentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    doctor = DoctorSerializer2()
    patient = PatientSerializer2()

    class Meta:
        model = Treatment
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    doctor = DoctorSerializer2()
    patient = PatientSerializer2()


    class Meta:
        model = Appointment
        fields = '__all__'


