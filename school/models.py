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

class Parent(models.Model):
    TITLE_CHOICES = [
        ("Dr", "Dr"),
        ("Mr", "Mr"),
        ("Mrs", "Mrs"),
        ("Miss", "Miss"),
        ("Prof", "Prof"),
        ("Madam", "Madam"),
    ]
    id_no = models.CharField(max_length=255)
    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title + " " + self.first_name + " " + self.last_name

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    admission_no = models.CharField(max_length=255)
    parent = models.ManyToManyField(Parent)
    in_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name + " " + self.last_name

class Teacher(models.Model):
    TITLE_CHOICES = [
        ("Dr", "Dr"),
        ("Mr", "Mr"),
        ("Mrs", "Mrs"),
        ("Miss", "Miss"),
        ("Prof", "Prof"),
        ("Madam", "Madam"),
    ]
    id_no = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    teaching = models.ManyToManyField(StudentClass)

    def __str__(self):
        return self.title + " " + self.first_name + " " + self.last_name