#Django
from django.db import models
from django.db.models.base import Model


class Departments(models.Model):
    name = models.CharField(max_length=100)


class Employees(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_joining = models.DateField()
    photo = models.CharField(max_length=100)