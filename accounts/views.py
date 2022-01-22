from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    if request.method=='GET':
        return render(request, 'accounts/login.html')
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        print("Email:", email)
        print("Password:", password)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('login'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))