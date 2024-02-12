import requests
from django.shortcuts import render, redirect, HttpResponse
from .forms import AddWordForm
from .models import UserDictionary

api_url = "https://655.mtis.workers.dev/translate"


def words(request):
    if request.method == "GET":
        form = AddWordForm()
        words = UserDictionary.objects.filter(user=request.user.id).all()
        return render(request, 'add_word.html', {'form': form, 'words': words})
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

                word.translation = translated_text
            else:
                print("Translated text not found in response")
            word.user = request.user
            word.save()
            return redirect('word_page', pk=word.id)


def word_page(request, pk):
    if request.method == "GET":
        word = UserDictionary.objects.filter(user=request.user, id=pk).all()

        return render(request, 'word_page.html', {'word': word})
    return HttpResponse('Random word')
