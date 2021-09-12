#Django
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
#Rest_framework
from rest_framework.parsers import JSONParser
#Employee Models
from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import *


@csrf_exempt
def deparmentApi(request, id=0):
    """CRUD Department"""
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse('Added Succesfully!!', safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(id=department_data["id"])
        departments_serializer = DepartmentSerializer(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse('Updated Succesfully!!', safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method == 'DELETE':
        department = Departments.objects.get(id=id)
        department.delete()
        return JsonResponse("Delete Successfully!!", safe=False)

@csrf_exempt
def employeetApi(request, id=0):
    """CRUD Employees"""
    if request.method == 'GET':
        employee = Employees.objects.all()
        employee_serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse('Added Succesfully!!', safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(id=id)
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse('Updated Succesfully!!', safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method == 'DELETE':
        employee = Employees.objects.get(id=id)
        employee.delete()
        return JsonResponse("Delete Successfully!!", safe=False)


@csrf_exempt
def save_file(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)