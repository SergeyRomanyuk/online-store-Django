from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from contact_form.views import ContactCreate, success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('^cart/', include('cart.urls')),
    path(r'^orders/', include('orders.urls')),
    path('contactfrm/', ContactCreate.as_view(), name='contact_page'),
    path('success/', success, name='success_page'),
    path('', include('web.urls')),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)