from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import custom_login, RegisterView,ProfileView,ProfileListView,ProfileUpdateView,ChangePasswordView,DeleteProfileView,follow_func

app_name = 'accounts'
urlpatterns = [
    path('login/',custom_login,name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),


    path('profiles/',ProfileListView.as_view(),name='profiles'),
    path('<int:pk>/profile/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/update/', ProfileUpdateView.as_view(), name='update_profile'),
    path('profile/<int:pk>/change-password/',ChangePasswordView.as_view(), name='change_password'),
    path('profile/<int:pk>/delete/', DeleteProfileView.as_view(), name='delete_profile'),

    path('profile/<int:pk>/follow/',follow_func , name='follow'),
]
