from django.urls import path
from users import views

urlpatterns = [
    path('', views.user_page, name='user_page'),
    path('delete/', views.user_delete, name='user_delete'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout')
]
