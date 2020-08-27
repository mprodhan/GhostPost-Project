from django import forms
from shostpost_app.models import GhostPost


class GhostPostForm(forms.Form):
    is_boast = forms.BooleanField(required=False)
    post = forms.CharField(max_length=280)