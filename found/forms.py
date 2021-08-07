
from django import forms

from .models import TweetFoundModel

from django.forms import ModelForm


class ImageExampleForm(ModelForm):
    class Meta:
        model = TweetFoundModel
        fields = ['image']