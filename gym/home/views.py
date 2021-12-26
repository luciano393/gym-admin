from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Discount, Partner, Pay, Plane
import json

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    partners = Partner.objects.all()
    plans = Plane.objects.all()
    discounts = Discount.objects.all()
    context = {'partners': partners, 'plans': plans, 'discounts': discounts }
    return render(request, 'home.html', context)

# Create your views here.
class PartnerView(View):
    """ @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs) """

    def get(self, request):
        partner = list(Partner.objects.values())
        if partner:
            data = { 'message' : "Success", "Partner": partner }
        else: 
            data = { 'message' : "Partner not found" }
            return JsonResponse(data)
    
    def post(self, request):
        jd = json.loads(request.body)
        Partner.objects.create(first_name=jd['first_name'], last_name = jd['last_name'], state = jd['state'], effective_date = jd['effective_date'], plane = jd['plane'], discounts = jd['discounts'])
        data = { 'message' : "Success" }
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        partners = list(Partner.objects.filter(id=id).values())
        if len(partners > 0):
            partner = Partner.objects.get(id=id)
            partner.first_name = jd['first_name']
            partner.last_name = jd['last_name']
            partner.state = jd['state']
            partner.effective_data = jd['effective_data']
            partner.plane = jd['plane']
            partner.discounts = jd['discounts']
            partner.save()
            data = { 'message' : "Success" }
        else:
            data = { 'message' : "Partner not found..."}
        return JsonResponse(data)

    def delete(self, request, id):
        partners = list (Partner.objects.filter(id=id).values())
        if len(partners) > 0:
            Partner.objects.filter(id=id).delete()
            data = { 'message': "Success" }
        else:
            data = { 'message': "Partner not found..."}
        return JsonResponse(data)

class PlaneView(View):
    def get(self, request):
        plane = list(Plane.objects.values())
        if plane:
            data = { 'message' : "Success", "Plane": plane }
        else: 
            data = { 'message' : "Plane not found" }
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Plane.objects.create(name=jd['name'], price = jd['price'])
        data = { 'message' : "Success" }
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        plans = list(Plane.objects.filter(id=id).values())
        if len(plans > 0):
            plane = Plane.objects.get(id=id)
            plane.name = jd['name']
            plane.price = jd['price']
            plane.save()
            data = { 'message' : "Success" }
        else:
            data = { 'message' : "Plane not found..."}
        return JsonResponse(data)

    def delete(self, request, id):
        plans = list (Plane.objects.filter(id=id).values())
        if len(plans) > 0:
            Plane.objects.filter(id=id).delete()
            data = { 'message': "Success" }
        else:
            data = { 'message': "Plane not found..."}
        return JsonResponse(data)

class DiscountView(View):
    def get(self, request):
        discoint = list(Discount.objects.values())
        if discoint:
            data = { 'message' : "Success", "Discoint": discoint }
        else: 
            data = { 'message' : "Discoint not found" }
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Discount.objects.create(name=jd['name'], percentage = jd['percentage'], applications = jd['applications'])
        data = { 'message' : "Success" }
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        discounts = list(Discount.objects.filter(id=id).values())
        if len(discounts > 0):
            discount = Discount.objects.get(id=id)
            discount.name = jd['name']
            discount.percentage = jd['percentage']
            discount.applications = jd['applications']
            discount.save()
            data = { 'message' : "Success" }
        else:
            data = { 'message' : "Discount not found..."}
        return JsonResponse(data)

    def delete(self, request, id):
        discounts = list (Discount.objects.filter(id=id).values())
        if len(discounts) > 0:
            Discount.objects.filter(id=id).delete()
            data = { 'message': "Success" }
        else:
            data = { 'message': "Discount not found..."}
        return JsonResponse(data)

class PayView(View):
    def get(self, request):
        pay = list(Pay.objects.values())
        if pay:
            data = { 'message' : "Success", "Pay": pay }
        else: 
            data = { 'message' : "Pay not found" }
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Pay.objects.create(partner=jd['partner'], discounts_applied = jd['discounts_applied'])
        data = { 'message' : "Success" }
        return JsonResponse(data)


    