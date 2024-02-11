from django.contrib import admin
from .models import UserProgress


class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'lessons', 'score')
    list_filter = ('user', 'lessons')


admin.site.register(UserProgress, UserProgressAdmin)
