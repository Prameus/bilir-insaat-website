from django.shortcuts import render
from api.models import Reffrences


def home(request, *args, **kwargs):
    return render(request, 'home.html')


def reference(request, *args, **kwargs):
    the_value = "Yol ve Köprü İnşaatı"
    reference_category = Reffrences.objects.filter(kategori=the_value)
    print(reference_category)

    return render(request, 'references.html', {'reference_category': reference_category})


def about(request, *args, **kwargs):
    return render(request, 'about.html')


def navbar(request, *args, **kwargs):
    return render(request, 'navbar.html')


def contact(request, *args, **kwargs):
    return render(request, 'contact.html')
