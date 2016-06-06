from django.conf.urls import url
from django.contrib import admin
from views import (
    ProductDetailView,
    ProductDownloadView,
    ProductListView,
    ProductRatingAjaxView,
    ProductUpdateView,
)

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name='detail_slug'),
    url(r'^(?P<pk>\d+)/download/$', ProductDownloadView.as_view(), name='download'),
    url(r'^(?P<slug>[\w-]+)/download$', ProductDownloadView.as_view(), name='download_slug'),
    url(r'^(?P<pk>\d+)/edit$', ProductUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/edit$', ProductUpdateView.as_view(), name='update_slug'),
    url(r'^ajax/rating/$', ProductRatingAjaxView.as_view(), name='ajax_rating'),
]
