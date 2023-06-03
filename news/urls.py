from django.urls import path
from django.views.decorators.cache import cache_page
from .views import (NewsList, PostDetail, PostSearch, NewsCreate,
                    NewsUpdate, NewsDelete, ArticleCreate, ArticleUpdate, ArticleDelete, CategoryList, subscribe,
                    unsubscribe, subscriptions)

urlpatterns = [
    path('news/', cache_page(3)(NewsList.as_view()), name='news_list'),
    path('news/<int:pk>', cache_page(30)(PostDetail.as_view()), name='post_detail'),
    path('articles/<int:pk>', cache_page(300)(PostDetail.as_view()), name='ar_detail'),
    path('news/search/', PostSearch.as_view(), name='search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/create/', ArticleCreate.as_view(), name='ar_create'),
    path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='ar_update'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='ar_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('categories/<int:pk>', CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
    path('categories/<int:pk>/unsubscribe', unsubscribe, name='unsubscribe'),

]
