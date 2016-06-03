from django.conf.urls import url
from django.contrib import admin
from views import (
    SellerDashboard,
)

urlpatterns = [
    url(r'^$', SellerDashboard.as_view(), name='dashboard'),
]
