from django.shortcuts import render
from django.views import View
from accounts.models import Owner, Tenant
from society.models import Flat, Society

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/index.html')

class OwnerView(View):
    def get(self, request, *args, **kwargs):
        owners = Owner.objects.all()
        context = {
            'owners': owners,
        }
        return render(request, 'dashboard/owners.html', context)
    
class TenantView(View):
    def get(self, request, *args, **kwargs):
        tenants = Tenant.objects.all()
        context = {
            'tenants': tenants,
        }
        return render(request, 'dashboard/tenants.html', context)

class SocietyView(View):
    def get(self, request, *args, **kwargs):
        societies = Society.objects.all()
        context = {
            'societies': societies,
        }
        return render(request, 'dashboard/societies.html', context)
    
class FlatView(View):
    def get(self, request, *args, **kwargs):
        flats = Flat.objects.all()
        context = {
            'flats': flats,
        }
        return render(request, 'dashboard/flats.html', context)