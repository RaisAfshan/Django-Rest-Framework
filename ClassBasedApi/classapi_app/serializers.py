from rest_framework import serializers

from classapi_app.models import Students


class StudentSerialize(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['name','course','age','college']