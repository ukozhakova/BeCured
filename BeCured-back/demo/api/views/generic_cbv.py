from django.shortcuts import render
from django.http import HttpResponse
from ..models import User, Doctor, Patient, Receptionist, Bills, Treatments, Appointments
from ..serializers import UserSerializer, DoctorSerializer, PatientSerializer, BillSerializer,\
    TreatmentSerializer, AppointmentSerializer, ReceptionistSerializer
from rest_framework import generics
from rest_framework.response import  Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404


class ReceptionistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Receptionist.objects.all()
    serializer_class = ReceptionistSerializer


class BillDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Bills.objects.all()
    serializer_class = BillSerializer


class TreatmentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Treatments.objects.all()
    serializer_class = TreatmentSerializer
