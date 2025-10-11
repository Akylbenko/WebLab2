from django.db import models

class Feedbacks(models.Model):
    name = models.CharField('Имя', max_length=50)
    email = models.EmailField('Почта', max_length=50)
    content = models.TextField('Комментарий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'