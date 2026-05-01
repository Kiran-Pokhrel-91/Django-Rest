from django.contrib import admin
from . models import Person

@admin.register(Person)

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','age']