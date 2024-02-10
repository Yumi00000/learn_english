from django.http import HttpResponse


def register(request):
    return HttpResponse('Welcome, new User!')


def login(request):
    return HttpResponse('Logged successfully!')


def logout(request):
    return HttpResponse('Logged out successfully!')


def user_page(request):
    if request.method == 'POST':
        return HttpResponse('User`s info edited')
    return HttpResponse('User`s info')


def user_delete(request):
    return HttpResponse('User successfully deleted')
