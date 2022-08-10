from typing_extensions import Required
from django.db import models

# Create your models here.
class County(models.Model):
    COUNTRY_CHOICE = [
        ("KE", "KE"),
    ]
    county_name = models.CharField(max_length=255, null=False)
    country = models.CharField(max_length=10, choices=COUNTRY_CHOICE, default="KE")

    def __str__(self):
        return self.county_name

class School(models.Model):
    school_name = models.CharField(max_length=255, null=False)
    county = models.ForeignKey(County, on_delete=models.CASCADE)

    def __str__(self):
        return self.school_name

class StudentClass(models.Model):
    class_name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_name

        