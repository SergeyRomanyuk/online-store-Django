from django.contrib import admin
from .models import Deliv
from .models import Contact
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created']
    list_filter = ['available', 'created']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)
# admin.site.register(Product)
admin.site.register(Deliv)
admin.site.register(Contact)

