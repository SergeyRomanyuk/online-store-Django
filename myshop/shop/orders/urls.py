from django.urls import path
from . import views


urlpatterns = [
    path(r'^create/', views.order_create, name='order_create'),
]