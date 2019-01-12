from django.shortcuts import render


def tweet_detail_view(request, id=1):
    """tweetの詳細を表示する"""
    return render(request, 'tweets/detail_view.html', {})


def tweet_list_view(request):
    """tweetの一覧を表示する"""
    return render(request, 'tweets/list_view.html', {})
