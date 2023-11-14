# from django.contrib import admin
# from .models import Contact, SpamNumber
# # Register your models here.
from django.contrib import admin
from .models import User, Contact, SpamNumber

admin.site.register(Contact)
admin.site.register(SpamNumber)
