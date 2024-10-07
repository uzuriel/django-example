from django.shortcuts import render
from .forms import *

def homepage(request):
    if request.POST:
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': AddProductForm(),
    }
    return render(request, 'homepage.html', context)