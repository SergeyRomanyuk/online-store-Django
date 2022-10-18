from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='home'),
    path('delivery/', views.delivery, name='delivery'), #шаблон URL-адреса для доставки
    path('contact/', views.contact, name='contact'), #шаблон URL-адреса для контактов
    path(r'^$', views.product_list, name='product_list'),
    path(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),




]