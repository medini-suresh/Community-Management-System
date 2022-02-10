from django.shortcuts import render
from django.views import View
from society.models import Flat, Society

# Create your views here.
def home(request):
    societies = Society.objects.all().order_by('updated_at')[:3]
    # print(flats)
    # d = {
    #     '1':2,
    #     '2':3,
    #     '3':1,
    # }
    # (1,2,3,4) #tuple -> Immutable
    # [1,2,3,4] #list -> Mutubale
    # print(d.items())
    for_frontend = {
        'societies': societies,
    }
    return render(request, 'society/index.html', for_frontend)

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'society/contact_us.html')
    