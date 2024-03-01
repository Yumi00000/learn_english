import random

import requests
from django.shortcuts import render, redirect

from scores.models import Score
from .forms import AddWordForm
from .models import UserDictionary

api_url = "https://655.mtis.workers.dev/translate"

from django.contrib.auth.decorators import login_required


@login_required(login_url='/user/login/')
def words(request):
    if request.method == "GET":
        form = AddWordForm()
        all_words = UserDictionary.objects.filter(user=request.user)
        return render(request, 'add_word.html', {'form': form, 'words': all_words})
    elif request.method == "POST":
        form = AddWordForm(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            trans_word_params = {
                'text': word.word,
                'source_lang': 'en',
                'target_lang': 'ru'
            }
            response = requests.get(api_url, params=trans_word_params)
            if response.status_code == 200:
                data = response.json()
                translated_text = data['response'].get('translated_text')

                word.translation = str(translated_text).lower()
            else:
                print("Translated text not found in response")

            word.user = request.user

            word.save()
            return redirect('/words/', pk=word.id)


# def word_page(request, pk):
#     if request.method == "GET":
#         word = UserDictionary.objects.filter(user=request.user, id=pk).all()
#
#         return render(request, 'word_page.html', {'word': word})
#     return HttpResponse('Random word')


def word_page(request, pk):
    message = None
    if request.method == "POST":
        test_word_id = request.POST.get('word_id')
        test_translation = request.POST.get('user_translate')

        test_word_in_db = UserDictionary.objects.get(id=test_word_id, user=request.user)
        print(test_word_in_db.word)

        if test_word_in_db is not None and test_word_in_db.translation == test_translation:
            message = 'Word is correct'
            score = Score.objects.get(user=request.user)
            score.value += 1
            score.save()
        else:
            message = 'Word is not correct'

    all_user_words = UserDictionary.objects.filter(user=request.user).all()
    random_word = random.choice(all_user_words)
    random_id = random_word.id
    word = UserDictionary.objects.get(user=request.user, id=pk)

    return render(request, 'word_checker.html', {'random_id': random_id, 'word': word, 'message': message})
