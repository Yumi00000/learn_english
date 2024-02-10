from django.contrib import admin
from words.models import UserDictionary


class UserDictionaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'word', 'translation', 'transcription', 'transliteration', 'audio')
    list_filter = ('user_id',)


admin.site.register(UserDictionary, UserDictionaryAdmin)
