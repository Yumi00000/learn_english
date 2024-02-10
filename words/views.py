from django.shortcuts import HttpResponse


def words(request):
    if request.method == "get":
        return 'New word added successfully'
    return HttpResponse('User`s words:')


def word_page(request, pk):
    if request.method == "get":
        return HttpResponse(f'Word {pk}')
    return HttpResponse('Random word')
