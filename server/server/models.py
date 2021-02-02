from django.db import models

class ShortLink(models.Model):
    origin = models.TextField(
        verbose_name='Оригинальная ссылка',
        max_length=1000
    )

    hash = models.CharField(
        verbose_name='Сокращенная ссылка',
        max_length=8
    )

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Сокращенная ссылка',
        verbose_name_plural = 'Сокращенные ссылки'
