from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def display_django_from(request):
    SFO=studentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        FO=studentForm(request.POST)
        if FO.is_valid():
            return HttpResponse(str(FO.cleaned_data))

    return render(request,'display_django_from.html',d)