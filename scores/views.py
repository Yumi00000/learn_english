from django.shortcuts import HttpResponse, render

from scores.models import Score


def top_scores(request):
    score = Score.objects.order_by('-value').all()
    return render(request, 'top_score.html', {'score': score})
