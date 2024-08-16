from django.shortcuts import render
from .models import Category, Item, Box
def items(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, 'item/items.html',{
        'items':items,
        'categories':categories,
    })

def box(request):
    boxs = Box.objects.all()
    return render(request, 'item/box.html',{
        'boxs':boxs,
    })