from ckeditor_uploader.fields import RichTextUploadingField
from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(verbose_name='Аватарка', upload_to='users/avatars/', null=True, blank=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ['id']

    def __str__(self):
        return '%s' % self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    Profile.objects.get_or_create(user=instance)


class Tags(models.Model):
    name = models.CharField(verbose_name='Название тега', max_length=30, unique=True)
    slug = models.SlugField(verbose_name='Адрес тега', max_length=30, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class CategoryOfArticles(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=30)
    slug = models.SlugField(verbose_name='Адрес категории', max_length=30, unique=True)
    icon = models.ImageField(verbose_name='Иконка категории', upload_to='category-icon/%Y/%m/%d/', null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Articles(models.Model):
    MODERATION = 0
    PENDING = 1
    PUBLISHED = 2
    STATUS = (
        (MODERATION, 'На модерации'),
        (PENDING, 'В ожидании'),
        (PUBLISHED, 'Опубликован')
    )

    owner = models.ForeignKey(AUTH_USER_MODEL, verbose_name='Автор', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(CategoryOfArticles, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Заголовок статьи', max_length=100)
    slug = models.SlugField(verbose_name='Адрес статьи', max_length=100)
    poster = models.ImageField(verbose_name='Постер/Изображение', upload_to='articles-poster/%Y/%m/%d/', null=True, blank=True)
    description = RichTextUploadingField(verbose_name='Описание')
    tags = models.ManyToManyField(Tags, verbose_name='Теги', blank=True)
    status = models.IntegerField(verbose_name='Статус', choices=STATUS, default=PUBLISHED)
    created_datetime = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)
    updated_datetime = models.DateTimeField(verbose_name='Дата и время изменения', auto_now=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title