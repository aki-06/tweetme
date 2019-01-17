from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
                        CreateView,
                        DeleteView,
                        DetailView,
                        ListView,
                        UpdateView
                        )
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, FormOwnerMixin
from .models import Tweet

class TweetCreateView(FormUserNeededMixin, CreateView):
    """tweetする"""
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/create/'


class TweetUpdateView(LoginRequiredMixin, FormOwnerMixin, UpdateView):
    """tweetを更新する"""
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = '/tweet/'


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    """tweetを削除する"""
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy('home')


class TweetDetailView(DetailView):
    """tweetの詳細に関するクラス"""
    queryset = Tweet.objects.all()


class TweetListView(ListView):
    """tweetの一覧を表示"""
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        """tweetのデータを取得"""
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context


