from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from tasks.constants import (
    DESCRIPTION_LENGTH_LIMIT, TITLE_LENGTH_LIMIT
)


class CustomUser(AbstractUser):
    """Переопределение стандартной модели пользователя."""

    email = models.EmailField('Электронная почта', unique=True)
    avatar = models.ImageField(
        'Аватар',
        upload_to='avatars/',
        blank=True,
        null=True
    )
    bio = models.TextField('О себе', blank=True, null=True)

    class Meta:
        """Мета-класс."""

        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Task(models.Model):
    """Модель задачи."""

    title = models.TextField(
        'Название',
        max_length=TITLE_LENGTH_LIMIT,
        blank=False
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    description = models.TextField(
        'Описание',
        max_length=DESCRIPTION_LENGTH_LIMIT,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    class Meta:
        """Мета-класс."""

        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title


class Habit(models.Model):
    """Модель привычек."""

    title = models.TextField(
        'Название',
        max_length=TITLE_LENGTH_LIMIT,
        blank=False
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    description = models.TextField(
        'Описание',
        max_length=DESCRIPTION_LENGTH_LIMIT,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    class Meta:
        """Мета-класс."""

        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

    def __str__(self):
        return self.title
