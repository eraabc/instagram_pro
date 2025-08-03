from django.contrib.auth import get_user_model
from django.db import models

class PostModel(models.Model):
    image = models.ImageField(upload_to='posts/',verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT,default=1,verbose_name='Автор',related_name='posts')

    def __str__(self):
        return self.description[:10]

    class Meta:
        db_table = 'post'
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
