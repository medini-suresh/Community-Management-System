from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from accounts.models import Owner, Tenant
from dashboard.forms import FlatForm
from society.models import Flat, Society

# Create your views here.
def dashboard(request):
    society_count = Society.objects.all().count()
    flat_count = Flat.objects.all().count()
    owner_count = Owner.objects.all().count()
    societies = Society.objects.all()
    context = {
        'society_count':society_count,
        'flat_count':flat_count,
        'owner_count':owner_count,
        'societies':societies,
    }
    return render(request, 'dashboard/index.html', context=context)

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

class SocietyDetail(View):
    def get(self, request, id, *args, **kwargs):
        society = Society.objects.get(id=id)
        flats = Flat.objects.filter(society=society)
        print(flats)
        context = {
            'society': society,
            'flats': flats,
        }
        return render(request, 'dashboard/society-detail.html', context)

class FlatView(View):
    def get(self, request, *args, **kwargs):
        flats = Flat.objects.all()
        context = {
            'flats': flats,
        }
        return render(request, 'dashboard/flats.html', context)
    
class FlatCreateView(View):
    def get(self, request, *args, **kwargs):
        form = FlatForm()
        context = {
            "form":form
        }
        return render(request, 'dashboard/flat-form.html', context)
    
    def post(self, request, id=None, *args, **kwargs):
        flat = Flat.objects.filter(id=id).first()
        form = FlatForm(request.POST)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('flats'))
        return render(request, 'dashboard/flat-form.html', {'form': form}) 
    
class FlatEditView(View):
    def get(self, request, id, *args, **kwargs):
        flat = Flat.objects.get(id=id)
        form = FlatForm(instance=flat)
        context = {
            "form":form
        }
        return render(request, 'dashboard/flat-form.html', context)
    
    def post(self, request, id, *args, **kwargs):
        flat = Flat.objects.get(id=id)
        form = FlatForm(request.POST, instance=flat)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('flats'))
        return render(request, 'dashboard/flat-form.html', {'form': form}) 