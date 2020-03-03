from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from news.models import Article
from api.serializers import ArticleSerializer

class ArticleList(APIView):
    def get(self, request):
        articles = Article.objects.all()[:20]
        data = ArticleSerializer(articles, many=True).data
        return Response(data)

class ArticleDetail(APIView):
    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        data = ArticleSerializer(article).data
        return Response(data)