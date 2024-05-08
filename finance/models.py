from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    company = models.CharField(max_length=50)


class CashTag(models.Model):
    tag = models.CharField(max_length=50)


class ManagerIO(models.Model):
    title = models.CharField(max_length=50)
    active = models.BooleanField()
    is_outcome = models.BooleanField(default=True, editable=False)
    value = models.DecimalField(max_digits=17, decimal_places=2)
    interval_start = models.DateField()
    interval_end = models.DateField(null=True)
    interval = models.CharField(max_length=30)
    # cash_tag_id = models.ForeignKey(CashTag, on_delete=models.SET_NULL, null=True)
    # company_id = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)


class BaseIO(models.Model):
    title = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=17, decimal_places=2)
    date = models.DateField()
    notes = models.TextField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)
    # manager_id = models.ForeignKey(ManagerIO, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True
        ordering = ['-date', '-value']


class Outflow(BaseIO):
    prediction = models.BooleanField(default=True)


class Inflow(BaseIO):
    pass






