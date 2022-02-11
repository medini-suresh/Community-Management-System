from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('owner/', views.OwnerView.as_view(), name='owners'),
    path('tenant/', views.TenantView.as_view(), name='tenants'),
    path('flat/', views.FlatView.as_view(), name='flats'),
    path('flat/add', views.FlatCreateView.as_view(), name='add-flat'),
    path('flat/edit/<int:id>', views.FlatEditView.as_view(), name='edit-flat'),
    path('societies/', views.SocietyView.as_view(), name='societies'),
    path('societies/<int:id>', views.SocietyDetail.as_view(), name='society-detail'),
    # path('logout/', views.logout_view, name='logout'),
    # path('signup/', views.SignupView.as_view(), name='signup'),
]