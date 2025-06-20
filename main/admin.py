from django.contrib import admin
from .models import Item, Size, ItemImage, Order, OrderItem


@admin.action(description='Змінити автора на "admin"')
def make_admin(modeladmin, request, queryset):
    queryset.update(author='admin')


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 1


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'gender')
    list_filter = ('type', 'sizes', 'gender')
    search_fields = ('title', 'description')
    filter_horizontal = ('sizes',)
    inlines = [ItemImageInline]


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'created_at')
    search_fields = ('full_name', 'phone_number', 'address')
    list_filter = ('created_at',)
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'item', 'quantity', 'price')
    list_filter = ('item',)
