from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, default="company_name")