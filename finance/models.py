from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    company = models.CharField(max_length=50)


class CashTag(models.Model):
    tag = models.CharField(max_length=50)


class Currency(models.Model):
    name = models.CharField(max_length=30)
    symbol = models.CharField(max_length=3)
    iso_code = models.CharField(max_length=3)


class OneIO(models.Model):
    """
    didn't add - media link, user
    When user is deleted data should remain in final version
    TODO: add recurring parameter
    """
    is_outcome = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=17, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    date = models.DateField()
    future = models.BooleanField(default=True)
    cash_tag = models.ForeignKey(CashTag, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-value']

# TODO: after creating recurring manager try this idea
class MonthlyTotals(models.Model):
    _year = models.IntegerField(editable=False, null=False)
    _month = models.IntegerField(editable=False, null=False)
    outcomes = models.DecimalField(max_digits=19, decimal_places=2, default=0, null=False)
    incomes = models.DecimalField(max_digits=19, decimal_places=2, default=0, null=False)

    class Meta:
        unique_together = ('_year', '_month')

    # def get_or_create(self):
    #     if self.objects.get(_year__exact=)