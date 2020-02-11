from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books/$', views.book_list),
    url(r'^book/(?P<pk>\d+)/$', views.book_detail),
    url(r'^book/price/(?P<price>\d+)/$', views.book_list_age),
]