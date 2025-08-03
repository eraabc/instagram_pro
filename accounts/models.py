from django.contrib.auth.models import AbstractUser
from django.db import models




class MyUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', verbose_name='Аватарка')
    bio = models.TextField(verbose_name='Инфо о пользователе',blank=True,null=True)
    phone_number = models.CharField(verbose_name='Номер телефона',max_length=20,blank=True,null=True)
    gender = models.CharField(choices=[('male','мужчина'),('female','женщина'),('other','остальное')],
                              verbose_name='пол',max_length=10,blank=True,null=True)
