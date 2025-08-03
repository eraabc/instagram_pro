from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import custom_login, RegisterView,ProfileView,ProfileListView

app_name = 'accounts'
urlpatterns = [
    path('login/',custom_login,name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),


    path('profiles/',ProfileListView.as_view(),name='profiles'),
    path('<int:pk>/profile/', ProfileView.as_view(), name='profile'),
]
