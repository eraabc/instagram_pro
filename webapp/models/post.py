from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class PostModel(models.Model):
    image = models.ImageField(upload_to='posts/',verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT,default=1,verbose_name='Автор',related_name='posts')


    def __str__(self):
        return self.description[:10]

    class Meta:
        db_table = 'post'
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'



class LikesModel(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='Тот кто лайкнул'
    )
    post = models.ForeignKey(
        PostModel,
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='Пост'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата лайка')

    class Meta:
        unique_together = ('user', 'post')
        db_table = 'like'
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    def __str__(self):
        return f"{self.user} нравится {self.post}"