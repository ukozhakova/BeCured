<<<<<<< HEAD
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ..models import Doctor, Patient, Rresponse, Rrequest
from ..serializers import DoctorSerializer2, PatientSerializer, RequestSerializer2, ResponseSerializer2


class PatientPage(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
=======
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Patient, Rrequest
from ..serializers import PatientSerializer, RequestSerializer2

#PATIENT
class patientLists(APIView):
    def get(self, request):
        patient_lists = Patient.objects.all()
        serializer = PatientSerializer(patient_lists, many=True)
>>>>>>> 45562c220a1878f12d8f789ae814645da8c53f64
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


<<<<<<< HEAD
class RequestPage(APIView):

=======
class patientListDetail(APIView):
    def get_object(self, pk):
        try:
            return Patient.objects.get(id=pk)
        except Patient.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        patient_lists = self.get_object(pk)
        serializer = PatientSerializer(patient_lists)
        return Response(serializer.data)

    def put(self, request, pk):
        patient_lists = self.get_object(pk)
        serializer = PatientSerializer(instance=patient_lists, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        patient_lists = self.get_object(pk)
        patient_lists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#REQUEST
class requestLists(APIView):
    def get(self, request):
        request_lists = Rrequest.objects.all()
        serializer = RequestSerializer2(request_lists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RequestSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class requestListDetail(APIView):
>>>>>>> 45562c220a1878f12d8f789ae814645da8c53f64
    def get_object(self, pk):
        try:
            return Rrequest.objects.get(id=pk)
        except Rrequest.DoesNotExist:
            raise Http404

    def get(self, request, pk):
<<<<<<< HEAD
        rrequest = self.get_object(pk)
        serializer = RequestSerializer2(request)
        return Response(serializer.data)

    def put(self, request, pk):
        rrequest = self.get_object(pk)
        serializer = RequestSerializer2(instance=request, data=request.data)
=======
        request_lists = self.get_object(pk)
        serializer = RequestSerializer2(request_lists)
        return Response(serializer.data)

    def put(self, request, pk):
        request_lists = self.get_object(pk)
        serializer = RequestSerializer2(instance=request_lists, data=request.data)
>>>>>>> 45562c220a1878f12d8f789ae814645da8c53f64
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
<<<<<<< HEAD
        rrequest = self.get_object(pk)
        rrequest.delete()
=======
        request_lists = self.get_object(pk)
        request_lists.delete()
>>>>>>> 45562c220a1878f12d8f789ae814645da8c53f64
        return Response(status=status.HTTP_204_NO_CONTENT)