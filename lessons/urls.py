from django.urls import path
from lessons import views

urlpatterns = [
    path('', views.lessons, name='lessons'),
    path('<int:pk>/', views.LessonsView.as_view(), name='lesson_page')
]
