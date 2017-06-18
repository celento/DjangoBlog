from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import Post

from . import views

urlpatterns = [
    #Using RegEx in Python 
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:50], template_name="blogapp/home.html")),

    #url for each individual posts
    url(r'^(?P<pk>\d+)', DetailView.as_view(model=Post, template_name= 'blogapp/post.html'))
    ]
