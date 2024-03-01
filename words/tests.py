from django.contrib.auth.models import User
from django.test import TestCase, Client

from scores.models import Score
from words.models import UserDictionary


class TestUserDictionary(TestCase):
    def setUp(self):
        new_user = User.objects.create_user(username='test1', password='test1')
        new_user.save()

    def test_add_words(self):
        client = Client()
        client.login(username='test1', password='test1')
        self.assertEqual(User.objects.get(username='test1').id, 1)
        response = client.post('/words/', {'word': 'word1'}, follow=True)
        self.assertEqual(response.status_code, 200)

        saved_word_count = UserDictionary.objects.filter(word='word1').count()
        self.assertEqual(saved_word_count,
                         1)


class TestWordRandomizer(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='test2', password='test2')
        self.new_user.save()
        score = Score.objects.create(user=self.new_user, value=0)
        score.save()
        self.client = Client()
        self.client.login(username='test2', password='test2')
        self.client.post('/words/', {'word': 'word'})
        self.client.post('/words/', {'word': 'gun'})
        self.client.post('/words/', {'word': 'apple'})

    def test_word(self):
        self.assertEqual(UserDictionary.objects.filter(word='word').count(), 1)
        self.assertEqual(UserDictionary.objects.filter(word='gun').count(), 1)
        self.assertEqual(UserDictionary.objects.filter(word='apple').count(), 1)
        print(UserDictionary.objects.filter(user=self.new_user).all().values())
        word1_id = UserDictionary.objects.get(word="word").id
        response = self.client.post(f'/words/{word1_id}/', {'word_id': f'{word1_id}', 'user_translate': 'слово'},
                                    follow=True)
        messages = response.context['message']
        self.assertEqual(str(messages), 'Word is correct')
        response = self.client.post(f'/words/{word1_id}/', {'word_id': f'{word1_id}', 'user_translate': 'c'},
                                    follow=True)
        messages = response.context['message']
        self.assertEqual(str(messages), 'Word is not correct')
        score = Score.objects.get(user=self.new_user)
        self.assertEqual(score.value, 1)
        self.assertEqual(response.status_code, 200)
        next_word = UserDictionary.objects.filter(word__in=['word', 'gun']).order_by('id').last()
        self.assertIn(next_word.word, ['gun', 'apple'])
