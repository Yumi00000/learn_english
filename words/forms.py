

from .models import UserDictionary

from django import forms


class AddWordForm(forms.ModelForm):
    class Meta:
        model = UserDictionary
        fields = ('word',)


