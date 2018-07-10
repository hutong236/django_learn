from .models import ActicleColumn,ArticlePost,Comment
from django import forms
from editormd.fields import EditorMdFormField


class ActicleColumnForm(forms.ModelForm):
    class Meta:
        model = ActicleColumn
        fields = ("column",)

class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ("title","body")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("commentator","body",)
