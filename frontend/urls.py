from django.urls import path
from .views import home, reference, about

urlpatterns = [
    path('', home),
    path('reference/', reference),
    path('about/', about)
]