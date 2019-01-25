from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
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
    # success_url = '/tweet/create/'


class TweetUpdateView(LoginRequiredMixin, FormOwnerMixin, UpdateView):
    """tweetを更新する"""
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    """tweetを削除する"""
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy('tweet:list')


class TweetDetailView(DetailView):
    """tweetの詳細に関するクラス"""
    queryset = Tweet.objects.all()


class TweetListView(ListView):
    """tweetの一覧を表示"""
    
    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        print(self.request.GET)
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
                )
        return qs

    def get_context_data(self, *args, **kwargs):
        """tweetのデータを取得"""
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy('tweet:create')
        return context


