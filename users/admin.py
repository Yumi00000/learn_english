from django.contrib import admin

from users.models.score import Score
from users.models.user import User
from users.models.user_dictionary import UserDictionary
from users.models.user_progress import UserProgress


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
