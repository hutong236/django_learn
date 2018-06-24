from .models import ActicleColumn
from django import forms


class ActicleColumnForm(forms.ModelForm):
    class Meta:
        model = ActicleColumn
        fields = ("column",)
