from django.shortcuts import render
from .models import Category, Item
def items(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, 'item/items.html',{
        'items':items,
        'categories':categories,
    })
