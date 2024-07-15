# bot_builder/forms.py
from django import forms
from .models import BotTemplate

class BotTemplateForm(forms.ModelForm):
    class Meta:
        model = BotTemplate
        fields = ['name', 'token', 'start_message']
