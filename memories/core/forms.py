from dataclasses import fields
from django import forms
from .models import MemoryPlace


class MemoryPlaceForm(forms.ModelForm):
    class Meta:
        model = MemoryPlace
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'long': forms.TextInput(attrs={'id': 'lng', 'class': 'form-control', 'readonly': 'readonly'}),
            'lat': forms.TextInput(attrs={'id': 'lat', 'class': 'form-control', 'readonly': 'readonly'}),
        }
        fields = ('name', 'comment', 'long', 'lat')
