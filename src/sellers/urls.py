from django.conf.urls import url
from django.contrib import admin

from products.views import (
    ProductCreateView,
    ProductUpdateView,
    SellerProductListView,
)
from views import (
    SellerDashboard,
    SellerProductDetailRedirectView,
    SellerTransactionListView,
)

urlpatterns = [
    url(r'^$', SellerDashboard.as_view(), name='dashboard'),
    url(r'^products/$', SellerProductListView.as_view(), name='product_list'),
    url(r'^products/add/$', ProductCreateView.as_view(), name='product_create'),
    url(r'^products/(?P<pk>\d+)/$', SellerProductDetailRedirectView.as_view()),
    url(r'^products/(?P<pk>\d+)/edit/$', ProductUpdateView.as_view(), name='product_update'),
    url(r'^transactions/$', SellerTransactionListView.as_view(), name='transactions'),
]
