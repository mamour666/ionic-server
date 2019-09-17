from django.contrib import admin
from .models import Category, Product, Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'adresse', 'productName', 'productQuantite']

admin.site.register(Order,OrderAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name','price']



admin.site.register(Product, ProductAdmin)
