# Generated by Django 2.1.7 on 2019-03-29 08:00

import autoslug.fields
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('www', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок статьи')),
                ('autoslug', autoslug.fields.AutoSlugField(editable=False, max_length=100, populate_from='title', verbose_name='Адрес статьи')),
                ('slug', models.SlugField(max_length=100, verbose_name='Адрес статьи')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='articles-poster/%Y/%m/%d/', verbose_name='Постер/Изображение')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('status', models.IntegerField(choices=[(0, 'На модерации'), (1, 'В ожидании'), (2, 'Опубликован')], default=2, verbose_name='Статус')),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_datetime', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='CategoryOfArticles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='Адрес категории')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='category-icon/%Y/%m/%d/', verbose_name='Иконка категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Название тега')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='Адрес тега')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users/avatars/', verbose_name='Аватарка'),
        ),
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.CategoryOfArticles', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='articles',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='articles',
            name='tags',
            field=models.ManyToManyField(blank=True, to='www.Tags', verbose_name='Теги'),
        ),
    ]