from typing_extensions import Required
from django.db import models

# Create your models here.
class County(models.Model):
    county_name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.county_name