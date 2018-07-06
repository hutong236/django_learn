from .models import ActicleColumn,ArticlePost
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

