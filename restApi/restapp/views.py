from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from restapp.models import Students
from restapp.serialize import Students_serialize


# Create your views here.
@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        data = Students.objects.all()
        serializer = Students_serialize(data,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = Students_serialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#PUT DELETE
@api_view(['PUT','DELETE','GET','PATCH'])
def del_edit(request,id):
    #EDIT
    try:
        obj = Students.objects.get(id=id)
    except Students.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Students_serialize(obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializers = Students_serialize(obj,request.POST)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=400)

    #DELETE

    elif request.method == 'DELETE':
        obj.delete()
        return Response(status=204)

    #PATCH
    elif request.method == 'PATCH':
        serializers = Students_serialize(obj, request.POST,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=400)







