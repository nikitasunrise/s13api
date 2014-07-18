from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import datetime

class BlogPost(models.Model):
    class Meta():
        db_table = 'posts'

    own_user = models.ForeignKey(User)
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('own_user', 'title', 'timestamp')

admin.site.register(BlogPost, BlogPostAdmin)
