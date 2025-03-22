from django.http import Http404
from django.shortcuts import render
from django.template.context_processors import request
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from employee_app.models import Employee
from employee_app.serializer import Employee_serializer


# Create your views here.

class EmployeeList(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self,request):
        obj = Employee.objects.all()
        serial = Employee_serializer(obj,many=True)
        return Response(serial.data)
    def post(self,request,format=None):
        serial = Employee_serializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

class EmployeeEdit(APIView):
    def get_object(self,id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            raise Http404

    def get(self,request,id):
        obj = self.get_object(id)
        serial =Employee_serializer(obj)
        return Response(serial.data)

    def put(self,request,id):
        obj =self.get_object(id)
        serial = Employee_serializer(obj,data=request.data,partial=True)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        self.get_object(id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






