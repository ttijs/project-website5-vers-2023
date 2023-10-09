from django.shortcuts import render # origineel
from django.shortcuts import render, redirect, get_object_or_404 # volgens tutorial


# Create your views here.
from .models import Werken

# Create your views here.
def home(request):
    werken = Werken.objects
    return render(request, 'werken/werken.html', {'werken': werken})

def detail(request, werken_id):
    werk = get_object_or_404(Werken, pk=werken_id)
    return render(request, 'werken/detail.html', {'werk': werk})