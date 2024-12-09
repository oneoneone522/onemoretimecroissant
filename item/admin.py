from django.contrib import admin

from .models import Category, Item, Box

admin.site.register(Item)
admin.site.register(Box)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')  # Display the 'name' and 'order' fields in the admin list view
    list_editable = ('order',)       # Allow the 'order' field to be editable directly in the admin list view
    ordering = ('order',) 