from django.contrib import admin

from components.models import Component, Category, Tag


# Register your models here.
@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    ...

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...