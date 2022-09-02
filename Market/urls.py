from django.urls import re_path as url, include
from . import views


app_name = 'Market'

# url(r'^orders/', include('orders.urls', 'orders'), namespace='orders'),
urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]










