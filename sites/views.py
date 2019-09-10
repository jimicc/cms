from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cards, Website, Cv, Cv_headline, Cv_list_element
from . import forms


def index(request):
    return render(request, 'sites/index.html')

def themes(request):
    cards = Cards.objects.all().order_by('title')
    return render(request, 'sites/themes.html', {'cards_dictionary':cards})
# Create your views here.

def website(request):
    website = Website.objects.all()
    return render(request, 'sites/website.html', {'website_detail': website})

def website_detailed(request, slug):
    website = Website.objects.get(slug=slug)
    return render(request, 'sites/new.html', {'website_detail': website})


def new(request):
    if request.method == 'POST':
        form = forms.CreateWebsite(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('sites:website')
    else:
        form = forms.CreateWebsite()
    return render(request, 'sites/create_website.html', {'form':form})

def cv(request):
    cv = Cv.objects.all()
    return render(request, 'sites/cv.html', {'cv_detail': cv})

def cv_detailed(request, slug):
    cv = Cv.objects.get(slug=slug)
    return render(request, 'sites/cv_new.html', {'cv_detail': cv, })

def cv_new(request):
    return render(request, 'sites/create_cv.html', )
