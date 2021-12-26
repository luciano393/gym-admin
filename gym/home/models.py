from django.db import models

# Create your models here.
class Plane(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Discount(models.Model):
    name = models.CharField(max_length=30)
    percentage = models.IntegerField()
    applications = models.IntegerField()

    def __str__(self):
        return self.name

class Partner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    state = models.BooleanField()
    effective_date = models.DateField()
    plane = models.ForeignKey(Plane, on_delete=models.SET_NULL , null=True, blank=True)
    discounts = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        name = self.first_name + ' ' + self.last_name
        return name

class Pay(models.Model):

    start_period = models.DateField(auto_now_add=True)
    end_period = models.DateField(auto_created=True)
    partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2, editable=False)
    discounts_applied = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True)

    def payment(self):
        pay =  self.discounts_applied.percentage * self.partner.plane.prince / 100
        self.amout = pay 
        return self

    def __str__(self):
        return self