from django.urls import re_path as url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


app_name = 'Market'


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include(('orders.urls', 'orders'), namespace='orders')),
    url(r'^', include('Market.urls', namespace='Market')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

