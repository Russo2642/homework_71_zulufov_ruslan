from django import forms
from posts.models import Comment
from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'description', 'author')
        labels = {
            'image': 'Картинка',
            'description': 'Описание'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')
