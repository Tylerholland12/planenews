
from django.urls import path
from news.views import ArticleListView, ArticleDetailView, ArticleCreateView


urlpatterns = [
    path('', ArticleListView.as_view(), name='news-list-page'),
    path('new-page/', ArticleCreateView.as_view(), name='news-new-page'),
    path('<str:slug>/', ArticleDetailView.as_view(), name='news-details-page'),

]
