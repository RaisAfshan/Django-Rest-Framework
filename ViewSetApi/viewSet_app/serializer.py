from rest_framework import serializers

from viewSet_app.models import Students


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields =['name','course']
