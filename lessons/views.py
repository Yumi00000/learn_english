import copy
import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from lessons.models import Lessons, Questions


def lessons(request):
    return HttpResponse('lessons')


class LessonsView(View):
    def get(self, request, pk):
        lesson = Lessons.objects.get(id=pk)
        questions = Questions.objects.filter(lesson_id=lesson).all()
        adjusted_questions = []
        for question in questions:
            current_question = {"question": question.question, "id": question.id}
            answers = [question.correct_answer] + question.wrong_answer.split('|')
            random.shuffle(answers)
            current_question["answers"] = answers
            adjusted_questions.append(copy.deepcopy(current_question))

        lesson_context = {"questions": adjusted_questions, "lesson": lesson}
        return render(request, 'lesson.html', lesson_context)

    def post(self, request, pk):
        lesson = Lessons.objects.get(id=pk)
        questions = Questions.objects.filter(lesson_id=lesson)
        results = []
        for question in questions:
            selected_answer = request.POST.get(f'questions_{question.id}')
            is_correct = True if selected_answer == question.correct_answer else False
            result_text = (f"{question.question} for your answer is: {selected_answer}"
                           f", correct answer is {question.correct_answer}; {is_correct}")

            results.append(result_text)
        return render(request, 'lesson_answers.html', {"results": results})
