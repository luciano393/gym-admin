from django.urls import path
from .views import DiscountView, PartnerView, PlaneView, home

urlpatterns = [
    path('', home, name='home'),
    path('api/partner/', PartnerView.as_view(), name='api/partner-list'),
    path('api/partner/<int:id>', PartnerView.as_view(), name='partner_process'),
    path('api/plane/', PlaneView.as_view(), name='plans_list'),
    path('api/plane/<int:id>', PlaneView.as_view(), name='plans_process'),
    path('api/discounts/', DiscountView.as_view(), name='discounts_list'),
    path('api/discounts/<int:id>', DiscountView.as_view(), name='discounts_process')
]