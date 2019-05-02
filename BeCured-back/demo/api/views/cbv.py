from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ..models import Doctor, Patient, Rresponse, Rrequest
from ..serializers import DoctorSerializer2, PatientSerializer, RequestSerializer2, ResponseSerializer2


class PatientPage(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RequestPage(APIView):

    def get_object(self, pk):
        try:
            return Rrequest.objects.get(id=pk)
        except Rrequest.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        rrequest = self.get_object(pk)
        serializer = RequestSerializer2(request)
        return Response(serializer.data)

    def put(self, request, pk):
        rrequest = self.get_object(pk)
        serializer = RequestSerializer2(instance=request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        rrequest = self.get_object(pk)
        rrequest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)