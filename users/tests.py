from django.contrib.auth.models import User
from django.test import TestCase, Client
from users.forms import UserRegisterForm, UserUpdateForm
from scores.models import Score


class RegisterTest(TestCase):
    def test_register_new(self):
        client = Client()
        response = client.post('/user/register/',
                               {'username': 'test', 'email': 'test@gmail.com', 'password': 'password',
                                'first_name': 'test', 'last_name': 'test',
                                'confirm_password': 'password'})
        self.assertEqual(response.status_code, 302)
        user_exists = User.objects.filter(username='test').all()
        self.assertTrue(user_exists.exists())
        self.assertEqual(len(user_exists), 1)
        user = User.objects.get(username='test')
        self.assertEqual(user.is_active, True)

    def test_register_confirm_password(self):
        client = Client()
        response = client.post('/user/register/',
                               {'username': 'test', 'email': 'test@gmail.com', 'password': 'password',
                                'first_name': 'test', 'last_name': 'test',
                                'confirm_password': 'password1'})
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message, 'Passwords do not match')

    def test_register_form(self):
        client = Client()
        form_data = {'username': 'test', 'email': 'test@gmail.com', 'password': 'password',
                     'first_name': 'test', 'last_name': 'test',
                     'confirm_password': 'password'}
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())
        form_data = {'username': 'test', 'email': 'testgmail.com', 'password': 'password',
                     'first_name': 'test', 'last_name': 'test',
                     'confirm_password': 'password'}
        response = client.post('/user/register/', form_data, follow=True)
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(response.status_code, 200)

    def test_register_get(self):
        client = Client()
        response = client.get('/user/register/')
        self.assertEqual(response.status_code, 200)


class UserProfileTest(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='test', email='test@gmail.com', password='password')
        self.new_user.save()
        Score.objects.create(user=self.new_user, value=0)

    def test_user_profile(self):
        client = Client()
        client.login(username='test', password='password')

        response = client.post('/user/',
                               {'username': 'test1', 'email': 'test1@gmail.com', 'first_name': 'test',
                                'last_name': 'test', 'password': 'passwordtest'}, follow=True)

        self.assertEqual(response.status_code, 200)
        saved_user = User.objects.get(username='test1')
        self.assertEqual(saved_user.first_name, 'test')
        self.assertEqual(saved_user.last_name, 'test')
        self.assertEqual(saved_user.email, 'test1@gmail.com')
        self.assertEqual(saved_user.password, 'passwordtest')
        self.assertEqual(saved_user.username, 'test1')
        client.login(username='test1', password='passwordtest')
        response = client.get('/user/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(saved_user.is_active, True)

    def test_user_profile_get(self):
        client = Client()
        client.login(username='test', password='password')
        response = client.get('/user/')
        self.assertEqual(response.status_code, 200)


class TestUserLogin(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='test2', password='password')
        self.new_user.save()

    def test_user_login(self):
        client = Client()
        response = client.post('/user/login/', {'username': 'test2', 'password': 'password'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.new_user.is_authenticated, True)

    def test_user_bad_login(self):
        client = Client()
        response = client.post('/user/login/', {'username': 'tes2t', 'password': 'password'})
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Invalid username or password')


class TestUserLogout(TestCase):
    def setUp(self):
        new_user = User.objects.create_user(username='test3', password='password')
        new_user.save()
        Score.objects.create(user=new_user, value=0)

    def test_user_logout(self):
        client = Client()
        client.post('/user/login/', {'username': 'test3', 'password': 'password'})
        response = client.post('/user/logout/')
        self.assertRedirects(response, '/user/login/')


class TestUserDelete(TestCase):
    def setUp(self):
        self.client = Client()
        self.new_user = User.objects.create_user(username='test4', password='password')
        self.new_user.save()

    def test_user_delete(self):
        self.client.post('/user/login/', {'username': 'test4', 'password': 'password'})
        self.client.post('/user/delete/')
        user = User.objects.filter(username='test3')
        self.assertFalse(user.exists())
