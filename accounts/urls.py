from django.urls import path

from accounts.views import custom_login, RegisterView

app_name = 'accounts'
urlpatterns = [
    path('login/',custom_login,name='login'),
    path('register/',RegisterView.as_view(),name='register'),
]
