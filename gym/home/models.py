from django.db import models

# Create your models here.
class Plane(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class Discounts(models.Model):
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    applications = models.IntegerField()

class Partner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    state = models.BooleanField()
    effective_date = models.DateField()
    plane = models.ForeignKey(Plane, on_delete=models.SET_NULL, null=True)
    discounts = models.ForeignKey(Discounts, on_delete=models.SET_NULL, null=True)

class Pay(models.Model):
    start_period = models.DateField(auto_now_add=True)
    end_period = models.DateField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True)
    discounts_applied = models.ForeignKey(Discounts, on_delete=models.SET_NULL, null=True)