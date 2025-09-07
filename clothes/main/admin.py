from django.contrib import admin
from .models import Product, Category, ProductSize, SubCategory, Order, OrderItem


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product_size', 'quantity')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'price', 'available',
        'created', 'updated'
    ]
    list_filter = [
        'available', 'created', 'updated'
    ]
    list_editable = [
        'price', 'available'
    ]
    prepopulated_fields = {
        'slug': ('name',)
    }
    inlines = [ProductSizeInline]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = [
        'paid', 'sent', 'created'
    ]
    list_filter = [
        'paid', 'sent', 'created'
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass