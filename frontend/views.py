from django.shortcuts import render
from api.models import Reffrences


def home(request, *args, **kwargs):
    return render(request, "home.html")


def reference(request, *args, **kwargs):
    reference_category = Reffrences.objects.values()
    the_array = []
    reference_len = len(reference_category)
    for y in range(reference_len):
        temp_array = []
        for i in range(1, 10):
            print(y)
            the_value = reference_category[y][f"referans_fotografi_{i}"]
            print(temp_array)
            if the_value != "":
                temp_array.append(the_value)
        the_array.append(temp_array)
        print(the_array)

    return render(request, "references.html", {"reference_category": the_array})


def about(request, *args, **kwargs):
    return render(request, "about.html")


def navbar(request, *args, **kwargs):
    return render(request, "navbar.html")


def contact(request, *args, **kwargs):
    return render(request, "contact.html")
