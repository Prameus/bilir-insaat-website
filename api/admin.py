from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Reffrences

admin.site.register(Reffrences)
admin.site.unregister(User)
admin.site.unregister(Group)
