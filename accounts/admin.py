from django.contrib import admin
from .models import *
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'date_created')
    list_display_links = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',
                    'description', 'date_created')
    list_display_links = ('name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_created', 'status')
    list_display_links = ('date_created',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Tag, TagAdmin)
