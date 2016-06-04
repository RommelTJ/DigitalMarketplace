from django.conf.urls import url
from django.contrib import admin
from views import (
    SellerDashboard,
    SellerTransactionListView,
)

urlpatterns = [
    url(r'^$', SellerDashboard.as_view(), name='dashboard'),
    url(r'^transactions/$', SellerTransactionListView.as_view(), name='transactions'),
]
