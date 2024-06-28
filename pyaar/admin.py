from django.contrib import admin
from .models import Animal, Details

# Register your models here.
admin.site.register(Details)
admin.site.register(Animal)