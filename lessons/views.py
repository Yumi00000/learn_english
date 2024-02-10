from django.http import HttpResponse


def lessons(request):
    return HttpResponse('lessons')


def lesson_page(request, pk):
    return HttpResponse(f'lesson_page {pk}')
