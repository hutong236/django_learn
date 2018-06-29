"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from article import views

urlpatterns = [
    url(r'^article-column/$',views.article_column,name='article_column'),
    url(r'^rename-column/$',views.rename_article,name='rename_article_column'),
    url(r'^del-column/$', views.delete_article_column, name='delete_article_column'),
    url(r'^article-post/$', views.article_post, name='article_post'),
]
