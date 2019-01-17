from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, FormOwnerMixin
from .models import Tweet

class TweetCreateView(FormUserNeededMixin, CreateView):
    """tweetするクラス"""
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/create/'


class TweetUpdateView(LoginRequiredMixin, FormOwnerMixin, UpdateView):
    """tweetを更新するクラス"""
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = '/tweet/'

class TweetDetailView(DetailView):
    """tweetの詳細に関するクラス"""
    queryset = Tweet.objects.all()

    # def get_object(self):
    #     """tweetの詳細をget"""
    #     return Tweet.objects.get(id=1)


class TweetListView(ListView):
    """tweetの一覧を表示"""
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        """tweetのデータを取得"""
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context


