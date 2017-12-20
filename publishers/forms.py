from django import forms
from .models import Publisher
from .validators import *

class PublisherCreateForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = [
            'website_address',
            'category',
            'name',
            'description',
            ]
