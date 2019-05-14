from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.dispatch import receiver
from ..models import Doctor, Patient, Treatment, Appointment, Profile, Receptionist
from ..serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer, TreatmentSerializer


@api_view(['GET', 'POST'])
def TreatmentLists(request):
    if request.method == 'GET':
        treatment_lists = Treatment.objects.all()
        serializer = TreatmentSerializer(treatment_lists, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TreatmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def TreatmentListsDetail(request, pk):
    try:
        treatment_lists = Treatment.objects.get(id=pk)
    except Treatment.DoesNotExist as e:
        return Response({'error': '{e}'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TreatmentSerializer(treatment_lists)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TreatmentSerializer(instance=treatment_lists, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
        treatment_lists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def create_user_profile(sender, instance, request, **kwargs):
    try:
        user_type = request.POST['usertype'].lower()
        if user_type == 'doctor':
            Doctor(user = instance).save()
        elif user_type == 'patient':
            Patient(user = instance).save()
        elif user_type == 'receptionist':
            Receptionist(user = instance).save()
        else:
            Profile(user = instance).save()
    except KeyError:
        Profile(user = instance).save()
