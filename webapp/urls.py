from django.urls import path

from webapp.views import IndexView, CreatePostView

app_name = 'webapp'
urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('create_post/',CreatePostView.as_view(),name='create_post'),
]
