from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..models import Doctor, Patient, Appointment, Treatment
from ..serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer, TreatmentSerializer
from django.http import Http404



class AppointmentLists(APIView):
    def get(self, request):
        appointment_lists = Appointment.objects.all()
        serializer = AppointmentSerializer(appointment_lists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AppointmentListDetail(APIView):

    def get_object(self, pk):
        try:
            return Appointment.objects.get(id=pk)
        except Appointment.DoesNotExist:
            raise Http404

    def get(self, request, pk):

        appointment_lists = self.get_object(pk)
        serializer = AppointmentSerializer(appointment_lists)
        return Response(serializer.data)

    def put(self, request, pk):
        appointment_lists = self.get_object(pk)
        serializer = AppointmentSerializer(instance=appointment_lists, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):

        appointment_lists = self.get_object(pk)
        appointment_lists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)