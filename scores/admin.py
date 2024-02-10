from django.contrib import admin

from scores.models import Score


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'value')
    search_fields = ('user',)


admin.site.register(Score, ScoreAdmin)
