from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from accounts.models import Owner, Tenant
from dashboard.forms import FlatForm, OwnerForm, SocietyForm, TenantForm
from society.models import Flat, Society
from django.contrib.auth.decorators import login_required


@login_required
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

def ListOwnerView(request):
        owners = Owner.objects.all()
        context = {
            'owners': owners,
        }
        return render(request, 'dashboard/owners.html', context)

def add_owner(request):
    if request.method == 'GET':
        form = OwnerForm()
        return render(request, 'dashboard/owner-form.html', context={'form':form})

    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('owners'))
        return render(request, 'dashboard/owner-form.html', context={'form':form})

def edit_owner(request, id):
    owner = Owner.objects.get(id=id)
    if request.method == 'GET':
        form = OwnerForm(instance=owner)
        return render(request, 'dashboard/edit-owner-form.html', context={'form':form, 'owner':owner})
    else:
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('owners'))
        return render(request, 'dashboard/edit-owner-form.html', context={'form':form, 'owner':owner})

def delete_owner(request, id):
    owner = Owner.objects.get(id=id)
    owner.delete()
    return HttpResponseRedirect(reverse('owners'))


def ListTenantView(request):
        tenants = Tenant.objects.all()
        context = {
            'tenants': tenants,
        }
        return render(request, 'dashboard/tenants.html', context)

def add_tenant(request):
    if request.method == 'GET':
        form = TenantForm()
        return render(request, 'dashboard/tenant-form.html', context={'form':form})

    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tenants'))
        return render(request, 'dashboard/tenant-form.html', context={'form':form})

def edit_tenant(request, id):
    tenant = Tenant.objects.get(id=id)
    if request.method == 'GET':
        form = TenantForm(instance=tenant)
        return render(request, 'dashboard/edit-tenant-form.html', context={'form':form, 'tenant':tenant})
    else:
        form = TenantForm(request.POST, instance=tenant)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tenants'))
        return render(request, 'dashboard/edit-tenant-form.html', context={'form':form, 'tenant':tenant})

def delete_tenant(request, id):
    tenant = Tenant.objects.get(id=id)
    tenant.delete()
    return HttpResponseRedirect(reverse('tenants'))

def ListSocietyView(request):
    societies = Society.objects.all()
    context = {
        'societies': societies,
    }
    return render(request, 'dashboard/societies.html', context)

def SocietyDetail(request, id):
    society = Society.objects.get(id=id)
    flats = Flat.objects.filter(society=society)
    print(flats)
    context = {
        'society': society,
        'flats': flats,
    }
    return render(request, 'dashboard/society-detail.html', context)

def add_society(request):
    if request.method == 'GET':
        form = SocietyForm()
        return render(request, 'dashboard/society-form.html', context={'form':form})

    if request.method == 'POST':
        form = SocietyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('societies'))
        return render(request, 'dashboard/society-form.html', context={'form':form})

def edit_society(request, id):
    society = Society.objects.get(id=id)
    if request.method == 'GET':
        form = SocietyForm(instance=society)
        return render(request, 'dashboard/edit-society-form.html', context={'form':form, 'society':society})
    else:
        form = SocietyForm(request.POST, instance=society)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('societies'))
        return render(request, 'dashboard/edit-society-form.html', context={'form':form, 'society':society})

def delete_society(request, id):
    society = Society.objects.get(id=id)
    society.delete()
    return HttpResponseRedirect(reverse('societies'))

def ListFlatView(request):
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
    
def edit_flat(request, id):
    flat = Flat.objects.get(id=id)
    if request.method == 'GET':
        form = FlatForm(instance=flat)
        return render(request, 'dashboard/edit-flat-form.html', context={'form':form, 'flat':flat})
    else:
        form = FlatForm(request.POST, instance=flat)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('flats'))
        return render(request, 'dashboard/edit-flat-form.html', context={'form':form, 'flat':flat})
    
def delete_flat(request, id):
    flat = Flat.objects.get(id=id)
    flat.delete()
    return HttpResponseRedirect(reverse('flats'))