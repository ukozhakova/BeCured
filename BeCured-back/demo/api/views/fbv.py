from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ..models import Doctor, Patient, Treatment, Appointment
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
        return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)

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