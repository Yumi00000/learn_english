from django.urls import path
from lessons import views

urlpatterns = [
    path('', views.lessons, name='lessons'),
    path('<int:pk>/', views.lesson_page, name='lesson_page')
]
