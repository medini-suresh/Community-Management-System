from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib import messages

from accounts.forms import CustomUserForm
from accounts.models import CustomUser

# Create your views here.
def login_view(request):
    if request.method=='GET':
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        return render(request, 'accounts/login.html')
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        print("Email:", email)
        print("Password:", password)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser or user.is_staff:
                return HttpResponseRedirect(reverse('dashboard'))
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('login'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

class SignupView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/signup.html')
    
    def post(self, request, *args, **kwargs):
        # print(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        aadhar = request.POST['aadhar']
        password = request.POST['password']
        form = CustomUserForm(request.POST)
        if form.errors:
            print(dir(form.errors))
            messages.warning(request, form.errors)
            return HttpResponseRedirect(reverse('signup'))
        user = CustomUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            aadhar=aadhar,
            password=password,
        )
        return HttpResponseRedirect(reverse('home'))