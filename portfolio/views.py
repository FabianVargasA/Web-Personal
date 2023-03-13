from django.shortcuts import render
from .models import project

# Create your views here.
def Portafolio(request):
    projects = project.objects.all()
    return render(request,"portfolio/portafolio.html", {'projects': projects})
