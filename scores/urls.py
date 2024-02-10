from django.urls import path
from scores import views

urlpatterns = [
    path('', views.top_scores, name='top_scores')

]
