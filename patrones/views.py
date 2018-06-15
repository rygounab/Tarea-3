from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def menu(request):
    data = {}
    template_name='menu.html'
    return render(request, template_name,data)

def mf(request):
    data = {}
    template_name='mostly_fluid.html'
    return render(request, template_name,data)

def cd(request):
    data = {}
    template_name='column_drop.html'
    return render(request, template_name,data)

def ls(request):
    data = {}
    template_name='layout_shifter.html'
    return render(request, template_name,data)
