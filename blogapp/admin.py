from django.contrib import admin
from .models import Post
# Registering our model for the admin access
admin.site.register(Post)
