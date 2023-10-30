from django.shortcuts import render
from .models import *

def home(request):
    sk = Skiils.objects.all()
    return render(request, 'root/index.html', context={sk:'sk'})
