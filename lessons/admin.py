

from django.contrib import admin
from lessons.models.lessons import Lessons
from lessons.models.questions import Questions


# Custom admin class for Lessons model
class LessonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


# Custom admin class for Questions model
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'wrong_answer', 'correct_answer', 'lesson_id')
    list_filter = ('lesson_id',)


# Register your models with custom admin classes
admin.site.register(Lessons, LessonsAdmin)
admin.site.register(Questions, QuestionsAdmin)
