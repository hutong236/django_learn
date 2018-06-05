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
from account import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #url(r'^login/$',views.user_login,name='user_login' ),
    #url(r'^login/$',auth_views.login,name='user_login' ),
    url(r'^new-login/$',auth_views.login,{"template_name": "account/login.html"},name='user_login' ),
    url(r'^logout/$',auth_views.logout,{"template_name": "account/logout.html"} ,name='user_logout'),
    url(r'^register/$', views.register,name='user_register'),
    url(r'^password-change/$',auth_views.password_change,{'post_change_redirect':'/account/password-change-done'},name='password_change'),
    url(r'^password-change-done/$',auth_views.password_change_done,name='password_change_done'),

]
