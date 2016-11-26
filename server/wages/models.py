from django.db import models


class Agency(models.Model):
    name = models.CharField(max_length=128)


class Department(models.Model):
    name = models.CharField(max_length=128)


class Title(models.Model):
    name = models.CharField(max_length=128)


class Wage(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=32)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    wage = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField(default=0)
