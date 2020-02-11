from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'city']

    def create(self, validated_data):
        employee = Employee(name=validated_data['name'], city=validated_data['city'])
        employee.save()
        return employee
