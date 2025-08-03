from django.urls import path

from accounts.views import custom_login

app_name = 'accounts'
urlpatterns = [
    path('login/',custom_login,name='login'),
]
