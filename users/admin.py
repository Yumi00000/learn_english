from django.contrib import admin
from .models import User, UserProgress


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'email', 'name', 'surname')
    search_fields = ('login', 'email', 'name', 'surname')


class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'lessons', 'score')
    list_filter = ('user', 'lessons')


admin.site.register(User, UserAdmin)

admin.site.register(UserProgress, UserProgressAdmin)
