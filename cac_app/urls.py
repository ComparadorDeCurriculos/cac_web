from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.compare, name='compare'),
    url(r'^result/(?P<i1>.+)/(?P<c1>.+)/(?P<i2>.+)/(?P<c2>.+)/$', views.result, name='result'),
]