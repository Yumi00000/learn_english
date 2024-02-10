from django.shortcuts import HttpResponse


def top_scores(request):
    return HttpResponse('Top scores:')
