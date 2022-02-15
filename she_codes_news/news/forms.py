from django import forms
from django.forms import ModelForm
from .models import NewsStory
from datetime import date

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'image', 'content']
        widgets = {
            'pub_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'value':date.today, 'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }