from django.shortcuts import render
from item.models import Category, Item

def index(request):
    items = Item.objects.filter(hot_item = True)[0:3]
    return render(request,'core/index.html',{
        'items':items,
    })
def news(request):
    return render(request, 'core/news.html')

def storeInfo(request):
    return render(request, 'core/storeInfo.html')