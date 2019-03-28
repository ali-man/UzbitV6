from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from www.models import Tags, CategoryOfArticles, Articles


class ArticleForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(), label='')
    title = forms.CharField(label='Заголовок', max_length=10)
    # category = forms.ModelChoiceField(queryset=CategoryOfArticles.objects.all())
    # tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all())

    class Meta:
        model = Articles
        fields = ['description', 'title', 'slug', 'category', 'poster', 'tags']
