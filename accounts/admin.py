from django.contrib import admin
from .models import CustomUser, Owner, Tenant
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Owner)
admin.site.register(Tenant)