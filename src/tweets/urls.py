from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', tweet_list_view, name='list'),
    url(r'^1/', tweet_detail_view, name='detal'),
]