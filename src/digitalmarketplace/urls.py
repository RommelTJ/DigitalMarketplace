from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from checkout.views import CheckoutTestView, CheckoutAjaxView
from dashboard.views import DashboardView

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'^checkout/$', CheckoutAjaxView.as_view(), name='checkout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/', include("products.urls", namespace='products')),
    url(r'^tags/', include("tags.urls", namespace='tags')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
