from django.contrib import admin
from .models import Item, Size, ItemImage


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

