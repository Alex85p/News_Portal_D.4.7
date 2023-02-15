from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'postCategory', 'title', 'text']
        labels = {
            'author': 'Автор',
            'postCategory': 'Категория',
            'title': 'Заголовок',
            'text': 'Текст новости',
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')

        if title == text:
            raise ValidationError(
                "Название новости не должно быть идентично ее содержанию."
            )

        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data['title']
        if title[0].islower():
            raise ValidationError(
                "Название новости должно начинаться с заглавной буквы"
            )
        return title


class ArticleForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    title = forms.CharField(max_length=50)
    default_data = {'category_type': 'Статья'}

    class Meta:
        model = Post
        fields = ['author', 'postCategory', 'title', 'text']
        labels = {
            'author': 'Автор',
            'postCategory': 'Категория',
            'title': 'Заголовок',
            'text': 'Текст новости',
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')

        if title == text:
            raise ValidationError(
                "Название статьи не должно быть идентично ее содержанию."
            )

        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data['title']
        if title[0].islower():
            raise ValidationError(
                "Название статьи должно начинаться с заглавной буквы"
            )
        return title
