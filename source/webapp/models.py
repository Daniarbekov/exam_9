from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Photo(models.Model):
    image = models.ImageField(
        verbose_name='Фотография', 
        upload_to='products'
    )
    note = models.CharField(
        verbose_name='подпись',
        max_length=100,
    )
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='reviews',
        on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
        )
    favorites = models.ManyToManyField(
        verbose_name='в избранных',
        related_name='photos',
        to=get_user_model())
