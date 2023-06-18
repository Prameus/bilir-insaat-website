from django.urls import path
from .views import home, reference

urlpatterns = [
    path('home/',home),
    path('reference/',reference)
]