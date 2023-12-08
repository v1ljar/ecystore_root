from django.contrib import admin
from .models import Product, Order, UserDetails

# Register your models here.
admin.site.register(Order)
admin.site.register(UserDetails)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'origin', 'brand')
    fieldsets = (
        ('Product Information', {
            'fields': ('title', 'price', 'origin', 'brand')
        }),
        ('Product Description', {
            'fields': ('description',)
        })
    )


admin.site.register(Product, ProductAdmin)
