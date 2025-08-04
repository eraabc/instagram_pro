from django.contrib.auth import get_user_model
from django.db import models


class Comment(models.Model):
   post = models.ForeignKey('webapp.PostModel', related_name='comments', on_delete=models.CASCADE, verbose_name='Пост')
   text = models.TextField(max_length=400, verbose_name='Комментарий')
   author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1, verbose_name='Автор',
                              related_name='comments')
   created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
   updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')


   def __str__(self):
       return self.text[:20]

   class Meta:
       db_table = 'comments'
       verbose_name = 'Коментарий'
       verbose_name_plural = "Коментарий"