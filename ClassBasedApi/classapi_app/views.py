
from rest_framework import status, generics

from classapi_app.models import Students
from classapi_app.serializers import StudentSerialize

# # Create your views here.
#
# class StudentList(APIView):
#     def get(self,request):
#         obj = Students.objects.all()
#         serial = StudentSerialize(obj,many=True)
#         return Response(serial.data)
#     def post(self,request):
#         serial = StudentSerialize(data=request.data)
#         if serial.is_valid():
#             serial.save()
#             return Response(serial.data,status=status.HTTP_201_CREATED)
#         return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
#
# class StudentEditList(APIView):
#    def get_object(self,id):
#         try:
#             return Students.objects.get(id=id)
#         except Students.DoesNotExist:
#             raise Http404
#     #EDIT
#    def get(self,request,id):
#         obj = self.get_object(id)
#         serial = StudentSerialize(obj)
#         return Response(serial.data)
#
#    def put(self,request,id):
#        obj = self.get_object(id)
#        serial = StudentSerialize(obj,data=request.data)
#        if serial.is_valid():
#            serial.save()
#            return Response(serial.data)
#        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
#
#    def delete(self,request,id):
#        self.get_object(id).delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
#
#
class StudentList(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerialize

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerialize
