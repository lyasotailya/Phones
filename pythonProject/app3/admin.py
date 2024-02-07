from django.contrib import admin

from app3.models import Phone


# Register your models here.


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'image', 'release_date', 'lte_exists', 'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}
