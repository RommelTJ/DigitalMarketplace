from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from checkout.views import CheckoutTestView, CheckoutAjaxView
from dashboard.views import DashboardView
from products.views import UserLibraryListView
from sellers.views import SellerDashboard

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'^checkout/$', CheckoutAjaxView.as_view(), name='checkout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/', include("products.urls", namespace='products')),
    url(r'^seller/', include("sellers.urls", namespace='sellers')),
    url(r'^tags/', include("tags.urls", namespace='tags')),
    url(r'^library/', UserLibraryListView.as_view(), name='library'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
