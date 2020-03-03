from rest_framework.serializers import ModelSerializer

from news.models import Article

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
