from rest_framework import serializers


class StaffSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    hire_date = serializers.DateField()
    position = serializers.CharField()
    department = serializers.CharField()