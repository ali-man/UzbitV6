# from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib.auth.models import User

from www.models import Tags, CategoryOfArticles, Articles


class ArticleForm(forms.ModelForm):
    owner = forms.ModelChoiceField(queryset=User.objects.all())
    description = forms.CharField(widget=CKEditorUploadingWidget(), label='')
    title = forms.CharField(label='Заголовок', max_length=100)
    slug = forms.CharField(label='Адрес статьи', max_length=100)
    category = forms.ModelChoiceField(queryset=CategoryOfArticles.objects.all(), label='Раз')
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all())

    class Meta:
        model = Articles
        fields = ['owner', 'description', 'title', 'slug', 'category', 'poster', 'tags']
