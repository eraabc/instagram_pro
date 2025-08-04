from django.contrib import admin

from webapp.models import Comment
from webapp.models.post import PostModel

admin.site.register(PostModel)
admin.site.register(Comment)