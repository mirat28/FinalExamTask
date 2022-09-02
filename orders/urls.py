from django.urls import re_path as url, include
from . import views


# app_name = 'orders'


urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    # url(r'^orders/', include('orders.urls', 'orders'), namespace='orders'),
]