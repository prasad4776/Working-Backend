from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .serializers import EmployeeSerializer
from .models import Employee

# Create your views here.

class EmployeeViewSet(ModelViewSet):

    serializer_class = EmployeeSerializer

    def list(self, request):
        data = Employee.objets.all()
        return {'message': data}

    def retrieve(self, request, pk):
        pass

    def
