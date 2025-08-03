from django.urls import path

from webapp.views import index, CreatePostView

app_name = 'webapp'
urlpatterns = [
    path('',index,name='index'),
    path('create_post/',CreatePostView.as_view(),name='create_post'),
]
