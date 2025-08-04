from django.contrib import admin

from webapp.models import Comment, LikesModel,PostModel

admin.site.register(PostModel)
admin.site.register(Comment)
admin.site.register(LikesModel)