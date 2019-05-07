from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Patient, Bill, Treatment, Doctor, Appointment, Receptionist
from ..serializers import PatientSerializer, AppointmentSerializer, BillSerializer, TreatmentSerializer


class PatientList(APIView):
    def get(self, request):
        patient_lists = Patient.objects.all()
        serializer = PatientSerializer(patient_lists, many=True)
        return Response(serializer.data)

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
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk):
        patient = self.get_object(pk)
        serializer = PatientSerializer(instance=patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid() and self.request.user.is_authenticated:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        patient = self.get_object(pk)
        if self.request.user.is_authenticated and self.request.user==patient.doctor:
            patient.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class AppointmentDetail(APIView):
    def get_object(self, pk):
        try:
            return Appointment.objects.get(id=pk)
        except Appointment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        appointment = self.get_object(pk)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid() and self.request.user.is_authenticated:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        appointment = self.get_object(pk)
        if request.user.is_authenticated and request.user == appointment.doctor:
            serializer = AppointmentSerializer(instance=appointment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

    def delete(self, request, pk):
        appointment = self.get_object(pk)
        if request.user.is_authenticated and request.user == appointment.doctor:
            appointment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class TreatmentDetail(APIView):
    def get_object(self, pk):
        try:
            return Treatment.objects.get(id=pk)
        except Treatment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        treatment = self.get_object(pk)
        serializer = TreatmentSerializer(treatment)
        return Response(serializer.data)

    def post(self, request):
        serializer = TreatmentSerializer(data=request.data)
        if serializer.is_valid() and self.request.user.is_authenticated:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        treatment = self.get_object(pk)
        if request.user.is_authenticated and request.user == treatment.doctor:
            serializer = TreatmentSerializer(instance=treatment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

    def delete(self, request, pk):
        treatment = self.get_object(pk)
        if request.user.is_authenticated and request.user == treatment.doctor:
            treatment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class BillDetail(APIView):
    def get_object(self, pk):
        try:
            return Bill.objects.get(id=pk)
        except Bill.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        bill = self.get_object(pk)
        serializer = BillSerializer(bill)
        return Response(serializer.data)

    def post(self, request):
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid() and self.request.user.is_authenticated:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        bill = self.get_object(pk)
        if request.user.is_authenticated and request.user == bill.doctor:
            serializer = BillSerializer(instance=bill, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

    def delete(self, request, pk):
        bill = self.get_object(pk)
        if request.user.is_authenticated and request.user == bill.doctor:
            bill.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
