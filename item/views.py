from django.shortcuts import render
from .models import Category, Item
def items(request):
    query = request.GET.get('query','')
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, 'item/items.html',{
        'items':items,
        'query':query,
        'categories':categories,
    })
