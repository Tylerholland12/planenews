from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    slug = models.CharField(max_length=200, blank=True, editable=False)
    content = models.TextField(
        help_text="Write the content of your page here.")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
  
        path_components = {'slug': self.slug}
        return reverse('news-details-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Article, self).save(*args, **kwargs)