from django.shortcuts import render
from item.models import Item
from .models import Carousel, News
def index(request):
    items = Item.objects.filter(hot_item = True)[0:3]
    context = {
        'repeat_count': range(20)  # 這裡定義要重複的次數
    }
    carousels = Carousel.objects.all()
    return render(request,'core/index.html',{
        'items':items,
        'carousels':carousels,
        'context':context,
    })
def news(request):
    news = News.objects.all()
    return render(request, 'core/news.html',{
        'news':news,
    })

def storeInfo(request):
    return render(request, 'core/storeInfo.html')