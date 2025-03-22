from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from viewSet_app.models import Students
from viewSet_app.serializer import StudentSerializer


# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend] # Class for searching or filtering
    filterset_fields  = ['course'] # field to search
    pagination_class = PageNumberPagination # used for pagination

