from django.shortcuts import render,get_object_or_404
from .models import BlogArticle

# Create your views here.

def blog_title(request):
    blogs = BlogArticle.objects.all()
    return render(request,"blog/title.html",{'blogs':blogs})

def blog_article(request,article_id):
    # article = BlogArticle.objects.get(id=article_id)
    article = get_object_or_404(BlogArticle,id=article_id)
    pub = article.publish
    dir(pub)
    return render(request,"blog/content.html",{"article":article,"publish":pub})
