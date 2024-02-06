from django.contrib import admin
from .models import User, Score, UserProgress, UserDictionary


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'email', 'name', 'surname')
    search_fields = ('login', 'email', 'name', 'surname')


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'value')
    list_filter = ('user',)


class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'lessons', 'score')
    list_filter = ('user', 'lessons')


class UserDictionaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'word', 'translation', 'transcription', 'transliteration', 'audio')
    list_filter = ('user',)


admin.site.register(User, UserAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(UserProgress, UserProgressAdmin)
admin.site.register(UserDictionary, UserDictionaryAdmin)
