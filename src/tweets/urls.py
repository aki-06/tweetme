from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='list'),
    url(r'^1/', TweetDetailView.as_view(), name='detal'),
]