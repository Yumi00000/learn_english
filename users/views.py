from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import QueryDict
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from scores.models import Score
from users.forms import LoginForm, UserRegisterForm, UserUpdateForm


def register(request):
    if request.method == 'GET':
        form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})
    elif request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
                messages.error(request, 'Passwords do not match')
                return render(request, 'register.html', {'form': form})
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password'], email=form.cleaned_data['email'],
                                            first_name=form.cleaned_data['first_name'],
                                            last_name=form.cleaned_data['last_name'])
            user.save()
            score = Score.objects.create(user=user, value=0)
            score.save()
            return redirect('/user/login/')
        else:
            return render(request, 'register.html', {'form': form})


def login_handler(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'authorization.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('/user/')

        messages.error(request, f'Invalid username or password')
        return render(request, 'authorization.html', {'form': form})


def logout_handler(request):
    from django.contrib.auth import logout
    if request.method == 'POST':
        logout(request)
    return redirect('/user/login/')


@login_required(login_url='/user/login/')
def user_page(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            if request.POST.get('_method') == 'PUT':
                put_data = QueryDict(request.POST.urlencode(), mutable=True)
                # put_data['password'] = form.cleaned_data['password']
                user = form.save(commit=False)
                # user.password = make_password(form.cleaned_data['password'])
                user.save()
            else:
                user.save()
            return redirect('/user/')
    else:
        user = request.user
        form = UserUpdateForm(instance=user)
        user_score = Score.objects.get(user=user)
        return render(request, 'user_page.html', {'form': form, 'user_score': user_score}, )


def user_delete(request):
    user = request.user
    if request.method == 'POST':
        user.delete()

    return redirect('/user/register/')
