from django.contrib import admin
from .models import Discount, Partner, Pay, Plane

# Register your models here.
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'state', 'effective_date', 'plane')

@admin.register(Plane)
class PlaneAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage', 'applications')

@admin.register(Pay)
class PayAdmin(admin.ModelAdmin):
    list_display = ('start_period', 'end_period', 'partner', 'discounts_applied', 'amount')
