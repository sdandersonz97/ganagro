from django.conf.urls import include, url
from . import views

app_name = 'ganagroapp'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^product/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.product_category, name='product_category'),
]
