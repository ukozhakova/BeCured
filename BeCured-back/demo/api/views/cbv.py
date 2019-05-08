from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ..models import Doctor, Patient, Appointments, Bills, Treatments, Receptionist
from ..serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer, \
    BillSerializer, TreatmentSerializer, ReceptionistSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PatientList(APIView):
    def get(self, request):
        patient_list = Patient.objects.all()
        serializer = PatientSerializer(patient_list, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PatientDetail(APIView):
    def get_object(self, pk):
        try:
            return Patient.objects.get(id=pk)
        except Patient.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        patient_list = self.get_object(pk)
        serializer = PatientSerializer(patient_list)
        return Response(serializer.data)

    def put(self, request, pk):
        patient_lists = self.get_object(pk)
        serializer = PatientSerializer(instance=patient_lists, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        patient_lists = self.get_object(pk)
        patient_lists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DoctorList(APIView):
    def get(self, request):
        doctor_list = Doctor.objects.all()
        serializer = DoctorSerializer(doctor_list, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DoctorDetail(APIView):
    def get_object(self, pk):
        try:
            return Doctor.objects.get(id=pk)
        except Doctor.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        doctor_list = self.get_object(pk)
        serializer = DoctorSerializer(doctor_list)
        return Response(serializer.data)

    def put(self, request, pk):
        doctor_list = self.get_object(pk)
        serializer = DoctorSerializer(instance=doctor_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        doctor_list = self.get_object(pk)
        doctor_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReceptionistDetail(APIView):

    def get_object(self, pk):
        try:
            return Receptionist.objects.get(id=pk)
        except Receptionist.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        receptionist_list = self.get_object(pk)
        if self.request.user.is_authenticated and self.request.user.username == receptionist_list.name:
            serializer = PatientSerializer(receptionist_list)
            return Response(serializer.data)

    def put(self, request, pk):
        receptionist = self.get_object(pk)
        if self.request.user.is_authenticated and self.request.user.username == receptionist.name:
            serializer = ReceptionistSerializer(instance=receptionist, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

    def delete(self, request, pk):
        receptionist = self.get_object(pk)
        if self.request.user.is_authenticated and self.request.user.username == receptionist.name:
            receptionist.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
