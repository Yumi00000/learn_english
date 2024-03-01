from django.contrib.auth.models import User
from django.test import TestCase, Client
from scores.models import Score


class ScoreTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='test', password='test')
        user2 = User.objects.create_user(username='test2', password='test2')
        user.save()
        user2.save()
        score = Score.objects.create(user=user, value='10')
        score2 = Score.objects.create(user=user2, value='20')
        score2.save()
        score.save()

    def test_score(self):
        client = Client()
        response = client.get('/scores/')
        self.assertEqual(response.status_code, 200)
