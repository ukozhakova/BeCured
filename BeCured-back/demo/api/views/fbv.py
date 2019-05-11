from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ..models import Doctor, Patient, Rresponse, Rrequest
from ..serializers import DoctorSerializer2, PatientSerializer, RequestSerializer2, ResponseSerializer2

#DOCTOR
@api_view(['GET', 'POST'])
def doctorLists(request):
    if request.method == 'GET':
        doctor_lists = Doctor.objects.all()
        serializer = DoctorSerializer2(doctor_lists, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DoctorSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




@api_view(['GET', 'PUT', 'DELETE'])
def doctorListDetail(request, pk):
    try:
        doctor_lists = Doctor.objects.get(id=pk)
    except Doctor.DoesNotExist as e:
        return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoctorSerializer2(doctor_lists)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DoctorSerializer2(instance=doctor_lists, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
        doctor_lists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# RESPONSE
@api_view(['GET', 'POST'])
def responseLists(request):
    if request.method == 'GET':
        rresponse_lists = Rresponse.objects.all()
        serializer = ResponseSerializer2(rresponse_lists, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ResponseSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def responseListDetail(request, pk):
    try:
        rresponse_lists = Rresponse.objects.get(id=pk)
    except Rresponse.DoesNotExist as e:
        return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ResponseSerializer2(rresponse_lists)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ResponseSerializer2(instance=rresponse_lists, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
        rresponse_lists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)