from django.urls import path

from webapp.views import IndexView, CreatePostView,UpdatePostView,DeletePostView,DetailPostView,AddCommentView,like_post,DeleteCommentView

app_name = 'webapp'
urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('create_post/',CreatePostView.as_view(),name='create_post'),
    path('post/<int:pk>/update/',UpdatePostView.as_view(),name='update_post'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('post/<int:pk>/',DetailPostView.as_view(),name='detail_post'),

    path('post/<int:pk>/add-comment/',AddCommentView.as_view(),name='add_comment'),
    path('comment/<int:pk>/delete/', DeleteCommentView.as_view(), name='delete-comment'),


    path('post/<int:pk>/like/', like_post, name='like_post'),
]
