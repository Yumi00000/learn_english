from django.contrib.auth.models import User

from .models import UserDictionary

from django import forms


class WordForm(forms.ModelForm):
    class Meta:
        model = UserDictionary
        user = forms.ModelChoiceField(queryset=User.objects.get(username=UserDictionary.user))
        fields = ('word', 'translation', 'transliteration', 'transcription', 'audio')
