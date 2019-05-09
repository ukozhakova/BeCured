from django.shortcuts import render
from django.http import HttpResponse
from ..models import User, Doctor, Patient, Receptionist, Bill, Treatment, Appointment
from ..serializers import UserSerializer, DoctorSerializer, PatientSerializer, BillSerializer,\
    TreatmentSerializer, AppointmentSerializer, ReceptionistSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404


class DoctorList(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        return Doctor.objects.for_user_order_by_name(self.request.user)

    def get_serializer_class(self):
        return DoctorSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientList(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        return Patient.objects.for_user_order_by_name(self.request.user)

    def get_serializer_class(self):
        return PatientSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer