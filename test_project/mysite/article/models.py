from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
from slugify import slugify

from mdeditor.fields import MDTextField
# Create your models here.

class ActicleColumn(models.Model):
    user = models.ForeignKey(User,related_name='article_column')
    column = models.CharField(max_length=200)
    create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column



class ArticlePost(models.Model):
    anthor = models.ForeignKey(User,related_name="article")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(ActicleColumn,related_name="article_column")
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("title",)
        index_together = (('id','slug'),)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(ArticlePost, self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("article:article_detail",args=[self.id,self.slug])



