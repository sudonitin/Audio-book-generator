from django.shortcuts import render
from django.http import HttpResponse
from .forms import contactForm

def contact(request):
    form = contactForm()
    return render(request, 'form.html', {'form': form})
# Create your views here.
