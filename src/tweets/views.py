from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin
from .models import Tweet

class TweetCreateView(FormUserNeededMixin, CreateView):
    """tweetするクラス"""
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/create/'


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


# def tweet_detail_view(request, id=1):
#     """tweetの詳細を表示する"""
#     obj = Tweet.objects.get(id=id)
#     print(obj)
#     context = {
#         'object': obj
#     }
#     return render(request, 'tweets/detail_view.html', context)


# def tweet_list_view(request):
#     """tweetの一覧を表示する"""
#     queryset = Tweet.objects.all()
#     print(queryset)
#     for obj in queryset:
#         print(obj.content)
#     context = {
#         'object_list': queryset
#     }
#     return render(request, 'tweets/list_view.html', context)
