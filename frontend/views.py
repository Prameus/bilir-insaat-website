from django.shortcuts import render

def home(request, *args, **kwargs):
    return render(request, 'home.html')

def reference(request,*args,**kwargs):
    return render(request, 'references.html')

def about(request, *args, **kwargs):
    return render(request, 'about.html')
