from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    path('owner/', views.ListOwnerView, name='owners'),
    path('owner/add', views.add_owner, name='add-owner'),
    path('owner/edit/<int:id>', views.edit_owner, name='edit-owner'),
    path('owner/delete/<int:id>', views.delete_owner, name='delete-owner'),

    path('tenant/', views.ListTenantView, name='tenants'),
    path('tenant/add', views.add_tenant, name='add-tenant'),
    path('tenant/edit/<int:id>', views.edit_tenant, name='edit-tenant'),
    path('tenant/delete/<int:id>', views.delete_tenant, name='delete-tenant'),

    path('flat/', views.ListFlatView, name='flats'),
    path('flat/add', views.FlatCreateView.as_view(), name='add-flat'),
    path('flat/edit/<int:id>', views.edit_flat, name='edit-flat'),
    path('flat/delete/<int:id>', views.delete_flat, name='delete-flat'),

    path('societies/', views.ListSocietyView, name='societies'),
    path('societies/<int:id>', views.SocietyDetail, name='society-detail'),
    path('society/add', views.add_society, name='add-society'),
    path('society/edit/<int:id>', views.edit_society, name='edit-society'),
    path('society/delete/<int:id>', views.delete_society, name='delete-society'),

    # path('logout/', views.logout_view, name='logout'),
    # path('signup/', views.SignupView.as_view(), name='signup'),
]