from django.shortcuts import render

from .models import Tweet


def tweet_detail_view(request, id=1):
    """tweetの詳細を表示する"""
    obj = Tweet.objects.get(id=id)
    print(obj)
    context = {
        'object': obj
    }
    return render(request, 'tweets/detail_view.html', context)


def tweet_list_view(request):
    """tweetの一覧を表示する"""
    queryset = Tweet.objects.all()
    print(queryset)
    for obj in queryset:
        print(obj.content)
    context = {
        'object_list': queryset
    }
    return render(request, 'tweets/list_view.html', context)
