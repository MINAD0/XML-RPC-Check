from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(UserProfile)
admin.site.register(Reservation)
admin.site.register(Fournisseurs)


