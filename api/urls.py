from django.urls import path

from api.views import ArticleList, ArticleDetail

urlpatterns = [
    path('articles/', ArticleList.as_view(), name='article_list'),
    path('articles/<int:pk>', ArticleDetail.as_view(), name='article_detail')
]