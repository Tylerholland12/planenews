import unittest

from django.test import TestCase, Client
from django.contrib.auth.models import User
from news.models import Article
from django.urls import reverse

class ArticleTestCase(TestCase):
    def test_true_is_true(self):

        self.assertEqual(True, True)

    def test_page_slugify_on_save(self):
        """Tests the slug generated when saving the article"""

        user = User()
        user.save()

        article = Article(title="My Test Page", content="test", author=user)
        article.save()
        self.assertEqual(article.slug, 'my-test-page')

class ArticleListViewTests(TestCase):

    def test_multiple_pages(self):
        user = User.objects.create()

        Article.objects.create(title="My Test Page", content="test", author=user)
        Article.objects.create(title="Another Test Page", content="test", author=user)

        #Make GET request
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

class ArticleDetailViewTests(TestCase):

    def test_page_loads_for_article(self, *args):
        user = User.objects.create()

        Article.objects.create(title="My Test Page", content="test", author=user)

        response = self.client.get('/my-test-page/')

        self.assertEqual(response.status_code, 200)