from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from news.forms import ArticleForm
from django.urls import reverse_lazy

from news.models import Article


class ArticleListView(ListView):

    model = Article

    def get(self, request):

        articles = self.get_queryset().all().order_by('-created')
        return render(request, 'list.html', {
          'articles': articles
        })

class ArticleDetailView(DetailView):

    model = Article

    def get(self, request, slug):
        """ Returns a specific of wiki page by slug. """
        article = get_object_or_404(Article, slug=slug)
        return render(request, 'page.html', context={'article': article})

class ArticleCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': ArticleForm()}
        return render(request, 'new.html', context)

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return HttpResponseRedirect(reverse_lazy('news-list-page'))

        return render(request, 'new.html', {'form': form})
