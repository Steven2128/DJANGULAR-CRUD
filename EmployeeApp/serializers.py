#Rest_framework
from django.db.models import fields
from rest_framework import serializers
from EmployeeApp import models
#EmployeeApp Models
from EmployeeApp.models import Departments, Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'