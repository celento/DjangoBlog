"""
Open source project created by Celento. Feel free to use it for anything cool.
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    #Django Admin Site
    url(r'^admin/', admin.site.urls),
    #Defining a URL path to our blog
    url(r'^', include('blogapp.urls')),
    
]
