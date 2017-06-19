from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import logout
from django.conf.urls.static import static
from django.conf import settings
app_name = 'ganagroapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.product_category, name='product_category'),
    url(r'^product/new/$', views.new_product, name='new_product'),

    url(r'^login/$',login,{'template_name':'login.html'}, name='login'),
    url(r'^logout/$',logout,{'template_name':'index.html'},name='logout'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.profile, name='profile'),
    url(r'^profile/(?P<pk1>[0-9]+)/product/(?P<pk>[0-9]+)/edit/$', views.edit_product, name='edit_product'),
    url(r'^new_user/$', views.register_user, name='new_user'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
