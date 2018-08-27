# dojo/forms.py
from django import forms
from . import validators

class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    content = forms.CharField(widget=forms.Textarea)