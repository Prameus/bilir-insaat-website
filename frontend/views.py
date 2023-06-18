from django.shortcuts import render

def home(request, *args, **kwargs):
    return render(request, 'home.html')

def reference(request,*args,**kwargs):
    return render(request, 'reference.html')