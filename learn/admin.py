from django.contrib import admin
from .models import Product, Access, Lesson, Group


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'start_date', 'cost']
    list_filter = ['start_date']
    search_fields = ['name', 'author__username']


@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']
    list_filter = ['product']
    search_fields = ['user__username', 'product__name']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'video_url']
    list_filter = ['product']
    search_fields = ['title', 'product__name']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'product', 'min_users', 'max_users']
    list_filter = ['product']
    search_fields = ['name', 'product.name']
    filter_horizontal = ('users',)
