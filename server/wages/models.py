from django.db import models


class Agency(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Wage(models.Model):
    first_name = models.CharField(db_index=True, max_length=64)
    last_name = models.CharField(db_index=True, max_length=64)
    middle_name = models.CharField(max_length=32)
    agency = models.ForeignKey(Agency, db_index=True, on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, db_index=True, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, db_index=True, on_delete=models.CASCADE)
    wage = models.DecimalField(db_index=True, max_digits=10, decimal_places=2)
    year = models.IntegerField(db_index=True, default=0)

    def serialize(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "middle_name": self.middle_name,
            "agency": self.agency.name,
            "dept": self.dept.name,
            "title": self.title.name,
            "wages": self.wage,
            "year": self.year,
        }

    def __str__(self):
        return '{last}, {first} {middle}'.format(
            last=self.last_name,
            first=self.first_name,
            middle=self.middle_name
        )
