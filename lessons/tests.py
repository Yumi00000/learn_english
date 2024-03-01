from django.test import TestCase, Client
from lessons.models import Lessons, Questions
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from scores.models import Score


class LessonsTestCase(TestCase):
    def setUp(self):
        new_user = User.objects.create_user(username='test', password='test')
        new_user.save()
        self.lesson = Lessons.objects.create(id=1, title='test title', body='test description')
        self.lesson.save()
        self.question = Questions.objects.create(lesson_id=self.lesson, question='test question',
                                                 wrong_answer='test wrong', correct_answer='test correct')
        self.question.save()

    def test_lessons_get(self):
        client = Client()
        client.login(username='test', password='test')
        response = client.get('/lessons/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(f'/lessons/{self.lesson.id}/')
        self.assertEqual(response.status_code, 200)


class QuestionsTestCase(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='test1', password='test1')
        self.lesson = Lessons.objects.create(id=1, title='test title', body='test description')
        self.question = Questions.objects.create(lesson_id=self.lesson, question='test question',
                                                 wrong_answer='test wrong', correct_answer='test correct')
        self.score = Score.objects.create(value=0, user=self.new_user)

    def test_questions_post(self):
        client = Client()
        client.login(username='test1', password='test1')
        response = client.post(f'/lessons/{self.lesson.id}/',
                               {f'questions_{self.question.id}': self.question.correct_answer}, follow=True)

        self.assertEqual(response.status_code, 200)

        self.score.refresh_from_db()
        self.assertEqual(self.score.value, 5)

        messages = [str(message) for message in get_messages(response.wsgi_request)]
        expected_message = (f"{self.question.question} for your answer is: {self.question.correct_answer},"
                            f" correct answer is {self.question.correct_answer}; True")
        self.assertIn(expected_message, messages)
