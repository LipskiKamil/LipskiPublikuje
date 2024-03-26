# w pliku forms.py
from ckeditor_uploader.fields import RichTextUploadingField
from django import forms
from .models import Comments, Articles
from .models import AboutMe
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['nickname', 'CommentContent']


class EditArticleForm(forms.ModelForm):
    content = RichTextUploadingField()

    class Meta:
        model = Articles
        fields = ['title', 'content', 'category', 'image', 'Fullimage']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'ckeditor'}),
        }