from django.urls import path
from .views import home, reference, about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
    path('reference/', reference),
    path('about/', about)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # pragma: nocover