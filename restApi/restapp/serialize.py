from rest_framework import serializers

from restapp.models import Students


class Students_serialize(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['name','course']

