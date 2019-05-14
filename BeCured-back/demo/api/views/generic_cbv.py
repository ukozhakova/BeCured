from django.shortcuts import render
from django.http import HttpResponse
from ..models import Doctor, Patient, Receptionist,  Treatment, Appointment
from ..serializers import  DoctorSerializer, PatientSerializer,\
    TreatmentSerializer, AppointmentSerializer, ReceptionistSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


class DoctorList(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        return Doctor.objects.all()

    def get_serializer_class(self):
        return DoctorSerializer

    def perform_create(self, serializer):
        serializer.save()


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class ReceptionistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Receptionist.objects.all()
    serializer_class = ReceptionistSerializer


class PatientList(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = (AllowAny, )

    # @login_required
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Patient.objects.all()
        # else:
        #     pass
        #     # return Patient.objects.get(self.request.user=doctor)

    def get_serializer_class(self):
        return PatientSerializer

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            serializer.save()


class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


# class PersonList(generics.ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer, DoctorSerializer
#     permission_classes = (IsAuthenticated, )
#
#     def get_queryset(self):
#         return Person.objects.all()
#
#     def get_serializer_class(self):
#         return PersonSerializer
#
#     def perform_create(self, serializer):
#             serializer.save()
