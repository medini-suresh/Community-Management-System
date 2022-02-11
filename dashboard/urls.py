from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('owner/', views.OwnerView.as_view(), name='owners'),
    # path('logout/', views.logout_view, name='logout'),
    # path('signup/', views.SignupView.as_view(), name='signup'),
]