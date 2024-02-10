from django.urls import path
from words import views
urlpatterns = [
    path('', views.words, name='user_dictionary'),
    path('<int:pk>/', views.word_page, name='word_page')
]
