from django.shortcuts import render
from item.models import Item
from .models import Carousel, News
def index(request):
    items = Item.objects.filter(hot_item = True)[0:3]
    carousels = Carousel.objects.all()
    return render(request,'core/index.html',{
        'items':items,
        'carousels':carousels,
    })
def news(request):
    news = News.objects.all()
    return render(request, 'core/news.html',{
        'news':news,
    })

def storeInfo(request):
    return render(request, 'core/storeInfo.html')