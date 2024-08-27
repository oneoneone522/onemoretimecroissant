from django.shortcuts import render
from item.models import Item
from .models import Carousel, Notification, News, Storeimg

def index(request):
    items = Item.objects.filter(hot_item = True)[0:3]
    context = {
        'repeat_count': range(20)  # 這裡定義要重複的次數
    }
    carousels = Carousel.objects.all()
    notices = Notification.objects.all()
    return render(request,'core/index.html',{
        'items':items,
        'carousels':carousels,
        'context':context,
        'notices':notices,
    })
def news(request):
    news = News.objects.all()
    return render(request, 'core/news.html',{
        'news':news,
    })

def storeInfo(request):
    storeImgs = Storeimg.objects.exclude(the_big=True)
    bigImg = Storeimg.objects.filter(the_big=True).first()
    return render(request, 'core/storeInfo.html',{
        'storeImgs':storeImgs,
        'bigImg':bigImg,
    })
