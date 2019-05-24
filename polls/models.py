# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create create the client table in the database
class Client(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact = models.CharField(max_length=21)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    upload = models.FileField()


class Employee(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact = models.CharField(max_length=21)
    Address = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)


class Delivery(models.Model):
    location = models.CharField
    upload = models.FileField()
    completed = False
    notes = models.CharField(max_length=250)
    paid = False
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Pharmacy(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=30, unique=True)
    contact = models.CharField(max_length=21)
    degarde = False


class Traditional(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=30, unique=True)
    contact = models.CharField(max_length=21)
