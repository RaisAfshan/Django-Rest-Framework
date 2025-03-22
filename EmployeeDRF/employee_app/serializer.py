from rest_framework import serializers

from employee_app.models import Employee


class Employee_serializer(serializers.ModelSerializer):
    profile_pic = serializers.FileField(required=False)  # or required=True, if image is mandatory

    class Meta:
        model = Employee
        fields = ['name','email','department','salary','data_joined','profile_pic']

