from django.urls import path

from webapp.views import IndexView, CreatePostView,UpdatePostView,DeletePostView,DetailPostView

app_name = 'webapp'
urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('create_post/',CreatePostView.as_view(),name='create_post'),
    path('post/<int:pk>/update/',UpdatePostView.as_view(),name='update_post'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('post/<int:pk>/',DetailPostView.as_view(),name='detail_post'),
]
