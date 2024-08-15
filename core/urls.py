from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('storeInfo', views.storeInfo, name='storeInfo'),
    ]